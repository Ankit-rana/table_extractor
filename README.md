
# Table Extractor

## Introduction

extractor is a tool to extract table from pdf and create excel out of it.

## Prerequisite

please install 2 dependencies. 
- Tkinter
- ghostscript
For ubuntu
```
apt install python3-tk ghostscript

```
Or For Centos
```
yum install tkinter ghostscript
```
```
$ virtualenv ENV
$ source ENV/bin/activate
$ pip3 install -r requirements.txt
```

## Installation

```
$ git clone https://github.com/Ankit-rana/table_extractor.git
$ cd table_extractor
$ sudo python3 setup.py install
```

## Steps

```
$ extractor sample.pdf 
$ ls
foo.xlsx
```
## Configuration

- extractor also provides ways to configure it. you can find configuration in /etc/extractor.conf
- take a look at the sample configuration file

```
[DEFAULT]
START_FIELD_NAME=Booking Date
DATEFIELDS=0,1,3 
AMOUNTFIELDS=4,5,6
```
