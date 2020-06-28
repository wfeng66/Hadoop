#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key     = key_value[0]   #key is first item in list
    value   = key_value[1]   #value is 2nd item 
	
    if (value.isdigit() or value[:3]=='ABC'):
        print('%s\t%s' % (key, value))   #print the <key \t value> 
	
	
