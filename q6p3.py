graph = dict()
with open('everybody_codes_e2024_q06_p3.txt','r') as infile:
	for line in infile:
		node, children = line.strip().split(':')
		children = children.split(',')
		if node not in graph:
			graph[node] = []
		for entry in children:
			if entry not in graph:
				graph[entry] = []
			graph[node].append(entry)

paths = []
lens = dict()

q=[('RR','')]
while q:
	loc, path = q.pop(0)
	if loc == '@':
		this_len = len(path+loc[0])
		paths.append((path+loc[0],this_len))
		if this_len not in lens:
			lens[this_len] = 1
		else:
			lens[this_len] += 1
	for entry in graph[loc]:
		if entry != 'ANT' and entry != 'BUG':
			q.append((entry, path+loc[0]))

for k,v in lens.items():
	if v == 1:
		unique_len = k
for p in paths:
	if p[1] == unique_len:
		print(p[0])
