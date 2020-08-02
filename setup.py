import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "table extractor",
    version = "0.0.1",
    author = "Ankit Rana",
    author_email = "connect.ankit.rana@gmail.com",
    description = ("An demonstration of how to extract table from pdf "
                                   "and create excel out of it."),
    packages=['table_extractor'],
    long_description=read('README.md'),
	data_files=[('/etc', ['extractor.conf'])],
    entry_points={
        'console_scripts': [
            'extractor=table_extractor.extractor:main',
        ],
    },
)
