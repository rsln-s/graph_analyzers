# Plan:
#
# 1. Open two files
# 2. Calculate cut for both
# 3. Maybe find the diff?.. (problem: parts might be inverted)

def calculate_cut(graph_file):
	graph_file_cut = 0
	for line in graph_file:
		data = [ float(x) for x in line.split() ]
		# data[0] is hedge num, data[1] is hedge weight, then it's data[2i-1]=vertex_num, data[2i]=part[vertex_num]
		curr_part=-1
		for i in range(3, len(data), 2):
			if curr_part == -1:
				curr_part = data[i]
				continue
			if curr_part != data[i]:
				graph_file_cut += data[1] #data[1] is hedge weight
				break

	return graph_file_cut

def run_calc(prefix, num_iter):
	out = []
	for it in range(1, num_iter):
		graph_name = (prefix+str(it))
		graph_file = open(graph_name, 'r')
		out.append(calculate_cut(graph_file))
	return out


def main():
	with_rs = run_calc("with_rs_", 9) 
	without_rs = run_calc("without_rs_", 9)
	for i in range(0, 8):
		print("iter: ", i+1 , " with_rs: ", with_rs[i], " without_rs ", without_rs[i])
	#print("iter: 23, with_rs: ", with_rs[i]," without_rs: N/A")

if __name__ == "__main__":
	main()
