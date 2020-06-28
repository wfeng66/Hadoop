#!/usr/bin/env python
import sys

show_cnts_to_output = [] #an empty list of day counts for a given word
prev_show = ""
prev_value = ""


for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_curr_value  = line.split('\t')   #split line, into key and curr_value, returns a list   

    curr_show  = key_curr_value[0]       #key is first item in list, indexed by 0
    curr_value   = key_curr_value[1]          #curr_value is 2nd item
    
    if(prev_show!=curr_show):
        if(prev_value[:3]=='ABC'):
            total_vws = sum(list(map(int, show_cnts_to_output)))  #count the sum of the list
            print('{0} {1}'.format(curr_show, total_vws))
        show_cnts_to_output=[]      #reset the list for new show
        show_cnts_to_output.append(curr_value)   #push the value to the list for sum later
    else:
        if (curr_value.isdigit()):           #After sorting by hadoop, the channel would sit on the end of show lists
            show_cnts_to_output.append(curr_value)   #push the value to the list for sum later
    prev_show = curr_show                    #reset the prev_show    
    prev_value = curr_value                  #reset the prev_value
    
