
scores = []
with open('everybody_codes_e2024_q07_p1.txt','r') as infile:
	for line in infile:
		total = 0
		char, moves = line.strip().split(':')
		power = 10
		for segment in moves.split(','):
			if segment == '+': power += 1
			if segment == '-': power -= 1
			power = max(0,power)
			total += power
		scores.append((char,total))
scores = sorted(scores, key=lambda x:x[1], reverse=True)
print(''.join(x[0] for x in scores))
