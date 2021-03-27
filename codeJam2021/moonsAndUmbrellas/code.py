#!/usr/bin/env python3

def calculate(x, y, s):
	costPer2chars = {
		'CJ' : int(x),
		'JC' : int(y)
	}
	ls = list(s)
	minCost = 0
	updatedLs = list()
	for elem in ls:
		if elem != '?':
			updatedLs.append(elem)
	ls = updatedLs
	for ind in range(len(ls) - 1):
		if ls[ind + 1] != ls[ind]:
			twoChars = ls[ind] + ls[ind + 1]
			#print(twoChars)
			minCost += costPer2chars[twoChars]
		#print("UpdatedCost", minCost)
		# else:
		# 	# There are basically two posibilities:C or J, will consider costing least
		# 	# Considering ? to be C:
		# 	myQuestion = 'C'
		# 	if myQuestion != ls[ind - 1] and 

	return minCost

t = int(input())
for case in range(t):
	x, y, s = [x for x in input().split()]
	print(f"Case #{case + 1}: {calculate(x, y, s)}")