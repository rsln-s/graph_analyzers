# Plan:
#
# 1. Open two files
# 2. Calculate cut for both
# 3. Maybe find the diff?.. (problem: parts might be inverted)

#graph_file = open('with_rs.txt', 'r')
graph_file = open('without_rs.txt', 'r')

#first, calculate cut for with_rs
graph_file_cut = 0
for line in graph_file:
	data = [ int(x) for x in line.split() ]
	# data[0] is hedge num, then it's data[2i-1]=vertex_num, data[2i]=part[vertex_num]
	curr_part=-1
	for i in range(2, len(data), 2):
		if curr_part == -1:
			curr_part = data[i]
			continue
		if curr_part != data[i]:
			graph_file_cut += 1
			break

print("Cut: ", graph_file_cut)
