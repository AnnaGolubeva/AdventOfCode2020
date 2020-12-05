import numpy as np


with open('input_day1.txt') as f: nums= f.read().splitlines()
nums = list(map(int, nums)) 

num_nums=len(nums)

for i in range(num_nums):
	for j in range(i+1,num_nums):
		for k in range(j+1,num_nums):
			sum_nums= nums[i]+nums[j]+nums[k]
			if sum_nums==2020:
				print(f'{nums[i]}*{nums[j]}*{nums[k]} = {nums[i]*nums[j]*nums[k]}')
				break



#=== from reddit ===#

#=== PART 1

# vals = map(int, nums)
# while vals:
#     x = vals.pop(0)
#     [print(x*v) for v in vals if x+v==2020]



