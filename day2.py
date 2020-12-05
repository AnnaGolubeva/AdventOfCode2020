import numpy as np


with open('input_day2.txt') as f: inp= f.read().splitlines()
#nums = list(map(int, nums))


def decompose_string(my_string):
	m, let, pw = my_string.split()
	let=let.strip(":")
	mi,ma = m.split("-")
	mi=int(mi)
	ma=int(ma)
	return mi, ma, let, pw


# PART 1
# 
# num_valid=0
# print(len(inp))
# for i in inp:
#	mi, ma, let, pw= decompose_string(i)
# 	num_occ= pw.count(let)
# 	if num_occ>=mi:
# 		if num_occ<=ma:
# 			num_valid+=1

# print(num_valid)



# PART 2
# given letter must be in exactly one of the positions

num_valid=0

for i in inp:
	mi, ma, let, pw= decompose_string(i)
	a= pw[mi-1]+pw[ma-1] # -1 because enumeration from 1, not 0
	if a.count(let)==1:
		num_valid+=1

print(num_valid)
