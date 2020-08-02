
# Table Extractor

## Introduction

extractor is a tool to extract table from pdf and create excel out of it.

## Installation

```
$ git clone <link to repo>
$ cd table_extractor
$ pip install develop
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
