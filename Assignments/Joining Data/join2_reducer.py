#!/usr/bin/env python
import sys

show_cnts_to_output = [] #an empty list of day counts for a given word

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list   

    curr_show  = key_value[0]       #key is first item in list, indexed by 0
    value   = key_value[1]          #value is 2nd item

    if (value.isdigit()):           #After sorting by hadoop, the channel would sit on the end of show lists
        show_cnts_to_output.append(value)   #If the value is digits, push it to the list for sum later
    else:                           #If the value isn't digits, it means reaching the end of specific show list
        total_vws = sum(list(map(int, show_cnts_to_output)))  #count the sum of the list
        print('{0} {1}'.format(curr_show, total_vws))
        show_cnts_to_output=[]      #reset the list for new show
    
