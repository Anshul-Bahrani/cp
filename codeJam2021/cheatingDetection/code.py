#!/usr/bin/env python3


# inputFromFile = open("input.txt", "r")

t = int(input())
p = int(input())
# print(t, p, inputFromFile.readline()[0])
ones = []
for case in range(t):
	answers = [0]*100
	for i in range(100):
		answers[i] = input()
	weight = [0]*10000
	for number in range(10000):
		ones = 0
		zeros = 0
		for contendor in range(100):
			if answers[contendor][number] == '1':
				ones += 1
			else:
				zeros += 1 
		weight[number] = zeros/ones
		# print(weight[0], weight[1], weight[2], ones, zeros)
	# print(weight[9999])
	cheatingProbability = [0]*100
	for contendor in range(100):
		for number in range(10000):
			cheatingProbability[contendor] += weight[number]*int(answers[contendor][number])
		cheatingProbability[contendor] /= answers[contendor].count('1')
		# cheatingProbability[contendor] = toAdd
	# print(cheatingProbability)
	# print("\n\n")
	# print(min(cheatingProbability) ,max(cheatingProbability), cheatingProbability[58])
	cheater = cheatingProbability.index(max(cheatingProbability))
	print(f"Case #{case + 1}: {cheater + 1}")
	# print(max(ones), min(ones), ones)