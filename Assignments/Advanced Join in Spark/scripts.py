show_views_file = sc.textFile("input/join2_gennum?.txt")
show_views_file.take(2)

def split_show_views(line):
    line = line.strip()
	key_value = line.split(',')
	show = key_value[0]
	views = int(key_value[1])
    return (show, views)


show_views = show_views_file.map(split_show_views)
show_views.take(5)
show_channel_file = sc.textFile("input/join2_genchan?.txt")


def split_show_channel(line):
	key_value = line.split(',')
	show = key_value[0]
	channel = key_value[1]
    return (show, channel)


show_channel = show_channel_file.map(split_show_channel)
joined_dataset = show_views.join(show_channel)


def extract_channel_views(show_views_channel): 
    views = show_views_channel[1][0]
    channel = show_views_channel[1][1]
    return (channel, views)
    
channel_views = joined_dataset.map(extract_channel_views)


def some_function(a, b):
    some_result = a+b
    return some_result


channel_views.reduceByKey(some_function).collect()