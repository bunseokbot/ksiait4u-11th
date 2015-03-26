import commands
from lib.dexparser import Dexparser
import sys
import os
import time
import re

#find regex param as array
def find_regex_listmode(strlist):
	tmpArray = []
	for string in strlist:
		url		= re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
		ip		= re.findall(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', string)

		#if email:
		#	tmpArray.append(str(email[0][0] + "@" + email[0][1]))
		
		if url:
			tmpArray.append(str(url[0]))
		
		if ip:
			tmpArray.append(str(ip[0]))

	return tmpArray

#find regex param as raw string
def find_regex_strmode(rawstr):
	tmpArray = []
	url     = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', rawstr)
	ip      = re.findall(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', rawstr)

	tmpArray.append(url)
	tmpArray.append(ip)
	return tmpArray

def cmp_dex2jar(dexfile):
	out = commands.getoutput("./lib/dex2jar/dex2jar.sh --force " + dexfile)
	outfname = '%s-dex2jar.jar' %(os.path.basename(dexfile).split('.')[0])
	f = open(outfname, 'rb')
	data = f.read()
	resultArr = find_regex_strmode(data)
	return resultArr

def cmp_dexparser(dexfile):
	d = Dexparser(dexfile) 
	data = d.string_list()
	resultArr = find_regex_listmode(data)
	return resultArr

d2jstarttime = time.time()
print "DEX2JAR Parse result : ", cmp_dex2jar(sys.argv[1])
d2jendtime = time.time()
print "DEX2JAR total time : %f" %float(d2jendtime - d2jstarttime)

parserstarttime = time.time()
print "DEXPARSER Parse result : ", cmp_dexparser(sys.argv[1])
parserendtime = time.time()
print "DEXPARSER total time : %f" %float(parserendtime - parserstarttime)
