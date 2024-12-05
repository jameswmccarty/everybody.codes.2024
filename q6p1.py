graph = dict()
with open('everybody_codes_e2024_q06_p1.txt','r') as infile:
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

q=[('RR','')]
while q:
	loc, path = q.pop(0)
	if loc == '@':
		paths.append(path+loc)
	for entry in graph[loc]:
		q.append((entry, path+loc))

for path in paths:
	print(path,len(path))
