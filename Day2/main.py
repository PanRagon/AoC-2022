import re

from input import input

arr = re.findall('..', input)
final_score = 0

def compete(match):
	if(match[0] == 'A' and match[1] == 'Z'):
		return 8
	elif(match[0] == 'A' and match[1] == 'Y'):
		return 4
	elif(match[0] == 'A' and match[1] == 'X'):
		return 3
	elif(match[0] == 'B' and match[1] == 'Z'):
		return 9
	elif(match[0] == 'B' and match[1] == 'Y'):
		return 5
	elif(match[0] == 'B' and match[1] == 'X'):
		return 1
	elif(match[0] == 'C' and match[1] == 'Z'):
		return 7
	elif(match[0] == 'C' and match[1] == 'Y'):
		return 6
	elif(match[0] == 'C' and match[1] == 'X'):
		return 2

for match in arr:
	final_score += compete(match)

print(final_score)