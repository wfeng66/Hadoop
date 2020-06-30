def split_fileA(line):
    line       = line.strip()       #strip out space
    key_value  = line.split(',')   #split line, into key and curr_value, returns a list  
    word       = key_value[0]
    count      = int(key_value[1])    
	return (word, count)
	
	