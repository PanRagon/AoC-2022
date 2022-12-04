from input import input;
import re;

sacks = input.split()

# Part 1
matchValues = 0

for sack in sacks:
    first, second = sack[:len(sack)//2], sack[len(sack)//2:]
    #print(first[0].isupper())
    common = ''.join(set(first).intersection(set(second)))
    matchValues += ord(common) - 38 if common.isupper() else ord(common) - 96

#Solution Part 1
print('Part one solution: ', matchValues)

# Part 2
groupSize = 3
groups = [sacks[i:i+groupSize] for i in range(0, len(sacks), groupSize)]
groupValues = 0

for group in groups:
    first, second, third = group[0], group[1], group[2]
    common = ''.join(set(first).intersection(set(second), set(third)))
    groupValues += ord(common) - 38 if common.isupper() else ord(common) - 96


#Solution Part 2
print('Part two solution: ', groupValues)