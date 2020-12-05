import numpy as np


with open('input_day2.txt') as f: inp= f.read().splitlines()
#nums = list(map(int, nums))


# PART 1
# num_valid=0
# print(len(inp))
# for i in inp:
# 	m, let, pw = i.split()
# 	mi,ma = m.split("-")
# 	mi=int(mi)
# 	ma=int(ma)
# 	let=let.strip(":")
# 	num_occ= pw.count(let)

# 	if num_occ>=mi:
# 		if num_occ<=ma:
# 			num_valid+=1

# print(num_valid)


# PART 2
num_valid=0

for i in inp:
	m, let, pw = i.split()
	mi,ma = m.split("-")
	mi=int(mi)
	ma=int(ma)
	let=let.strip(":")
	num_occ= pw.count(let)

	if num_occ>=mi:
		if num_occ<=ma:
			num_valid+=1

print(num_valid)
