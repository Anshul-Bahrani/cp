#!/usr/bin/env python3

def check(n, c):
	if c > ((n*(n + 1))//2) - 1 or c < n - 1:
		return False
	return True
def reverse(n, c):
	toReturn = []
	if not check(n, c):
		return "IMPOSSIBLE"
	fixed = 0
	jump = n - 1
	toMinus = jump
	toReturn = [x for x in range(1, n + 1)]
	c = c - jump
	# print("Init:", "C:", c, "toMinus", toMinus, "jump", jump)
	right = n
	left = 0
	counter = 3
	while(c != 0):

		if c >= toMinus:
			toReturn = toReturn[:left] + toReturn[right - 1:left:-1] + toReturn[left:left + 1] + toReturn[right:]
			fixed += 1
			if fixed%2 == 1:
				right -= 1
			else:
				left += 1
			
			c = c - toMinus
			jump -= 1
			toMinus = jump
		else: 
			# print("Left:", left, "Right:", right, "C:", c)
			# print(toReturn[:left], toReturn[left + c:left: -1], toReturn[left:left + 1] ,toReturn[left + c + 1:right] ,toReturn[right:])
			toReturn = toReturn[:left] + toReturn[left + c:left: -1] + toReturn[left:left + 1] + toReturn[left + c + 1:right] + toReturn[right:]
			# print("Small")
			break
		#print("C:", c, "toReturn:", toReturn)
		counter -= 1
	return toReturn

t = int(input())
for case in range(t):
	n,c = [int(x) for x in input().split()]
	answer = reverse(n, c)
	if not isinstance(answer, list):
		print(f"Case #{case + 1}: {answer}", end="")
	else:
		print(f"Case #{case + 1}:", end="")
		for elem in answer:
			print(f" {elem}", end="")
	print()