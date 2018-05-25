#!/usr/bin/python

#Testad i python3.6.

import re
import sys

print('......................................')
print('......................................')
print(' __x______ XML SMASHER v0.10 ______x__ ')
print('......................................')
print('......................................')
print(' ')
print(' ')

filin = input('Select xml-file to smash: ')
print(' ')
filut = input('Select output: ')
print(' ')

fu = open(filut, 'w')

try:
	fi = open(filin, 'r')

except (FileNotFoundError, NameError, PermissionError):
	print('File not found. Process killed.')
	exit()

for line in fi:
    result = re.search('(?<=\>)(.*)(?=<\/P>)' , line)
    if result:
    	print(result.group(0))
    	fu.write(result.group(0) + '\n')

fi.close()
fu.close()
