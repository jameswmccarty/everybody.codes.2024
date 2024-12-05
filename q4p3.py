with open('everybody_codes_e2024_q04_p3.txt','r') as infile:
	nails = [*map(int, infile.read().split())]

best = float('inf')
for target in nails:
	best = min(best, sum(abs(x-target) for x in nails))
print(best)
