#!/usr/bin/env python3

t = int(input())

for case in range(t):
	n = int(input())
	ls = [int(x) for x in input().split()]
	# print(ls[2::-1])
	cost = 0
	for i in range(n - 1):
		cost += 1
		if len(ls[i:n]) > 0:
			j = ls[i:n].index(min(ls[i:n])) + i
			cost +=	j - i
			# print("Before",ls[:i] ,ls[j:i:-1] ,ls[i:i + 1],ls[j + 1:])
			ls = ls[:i] + ls[j:i:-1] + ls[i:i+1] + ls[j + 1:]
			# print(i, j, ls, cost)
	print(f"Case #{case + 1}: {cost}")
