import camelot
import sys
import configparser


def get_context():
	context = {}
	config = configparser.ConfigParser()
	config.read("/etc/extractor.conf")
	for key in config['DEFAULT']:
		if key == 'start_field_name':
			context['table_start'] = config['DEFAULT'][key]
		if key == 'datefields':
			context['dates'] = [int(i) for i in config['DEFAULT'][key].split(',')]
		if key == 'amountfields':
			context['amounts'] = [int(i) for i in config['DEFAULT'][key].split(',')]
	return context

def dmy_to_ymd(dmy):
	d,m,y = dmy.split(".")
	return "/".join([y,m,d])

def format_amount(arg):
	return format(float(arg.replace(",", "")), ".2f")

def process(filename, context):
	# get tables with the help of camelot
	try:
		tables = camelot.read_pdf(filename, flavor='stream', strip_text='\n')
	except Exception as e:
		print(e)
		sys.exit(1)

	for i in range(len(tables)):
		# get a table
		dft = tables[i].df

		# detect start row of the table
		table_start_row = None
		for i in range(dft.shape[0]):
			if dft.loc[i, 0] == context.get('table_start'):
				table_start_row = i
				break

		# format columns with date if provided in config
		dft = dft.drop([32], axis=0)
		if context.get('dates'):
			for i in range(table_start_row+1, dft.shape[0]-2):
				for d in context.get('dates'):
					if dft.loc[i, d]:
						dft.loc[i, d] = dmy_to_ymd(dft.loc[i, d])

		# format columns with amount if provided in config
		if context.get('amounts'):
			for i in range(table_start_row+1, dft.shape[0]-2):
				for d in context.get('amounts'):
					if dft.loc[i, d]:
						dft.loc[i, d] = format_amount(dft.loc[i, d])

		# clear content above table if start row provided
		if table_start_row:
			dt = [i for i in range(table_start_row)]
			dft = dft.drop(dt, axis=0)
		else:
			table_start_row = 0

		# process rows spreading on multiple lines
		di = []
		for i in range(dft.shape[0]-2, table_start_row, -1):
			if not dft.loc[i, 0] and not dft.loc[i, 1]:
				# add content to previous row.
				for j in range(dft.shape[1]):
					dft.loc[i-1, j] += dft.loc[i, j].strip()
				# record drop of current row
				di.append(i)
		dft = dft.drop(di, axis=0)

		# export to spreadsheet
		dft.to_excel("foo.xlsx", header=False, index=False)

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	else:
		print("usage: extractory <filename>")
		sys.exit(1)
	context = get_context()
	process(filename, context)

if __name__ == "__main__":
	main()

