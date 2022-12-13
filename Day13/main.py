from ast import literal_eval
from test import test_input

from input import input

#Init
parse = test_input.split('\n\n')
packet_pairs = []
for pair in parse:
    pair = pair.split('\n')
    packet_pairs.append([literal_eval(pair[0]), literal_eval(pair[1])])

print(packet_pairs)
correct = 0

def compare_list(l, r):
    ordered = True
    for i in range(0, len(l)):
        print('Length: ', len(r))
        if(i >= len(r)):
            return False
        if(type(l[i]) is not type(r[i])):
            print(l[i], 'does not match', r[i])
            if (type(l[i]) is int):
                l[i] = [l[i]]
            else:
                r[i] = [r[i]]
            ordered = compare_list(l[i], r[i])
        if(type(l[i]) is list):
            ordered = compare_list(l[i], r[i])
        if(l[i] > r[i]):
            return False
    
    return ordered

for idx, pair in enumerate(packet_pairs):
    if(compare_list(pair[0], pair[1])):
        print('Correct: ', idx+1)
        correct += idx+1
    else:
        print('Incorrect: ', idx+1)
print(correct)