with open('everybody_codes_e2024_q04_p2.txt','r') as infile:
	nails = [*map(int, infile.read().split())]

lowest = min(nails)
print(sum(x-lowest for x in nails))
