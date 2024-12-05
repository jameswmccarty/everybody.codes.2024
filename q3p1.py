grid = dict()

with open('everybody_codes_e2024_q03_p2.txt','r') as infile:
	y = 0
	for line in infile:
		for x, char in enumerate(line.strip()):
			if char == '.':
				grid[(x,y)] = 0
			else:
				grid[(x,y)] = 1
		y += 1

while True:
	new_grid = dict()
	dug = False
	for k,v in grid.items():
		x,y = k
		if v > 0 and all(((x+dx,y+dy) in grid and grid[(x+dx,y+dy)] == v) for dx,dy in ((0,1),(0,-1),(1,0),(-1,0))):
			new_grid[(x,y)] = v+1
			dug = True
		else:
			new_grid[(x,y)] = v
	grid = new_grid
	if not dug:
		break

print(sum(v for v in grid.values()))
