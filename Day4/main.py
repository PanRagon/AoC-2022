from input import input
pairs = input.split()

#Part 1
subsets = 0

for pair in pairs:
    pair_list = pair.split(',')
    first_set = set(range(int(pair_list[0].split('-')[0]), int(pair_list[0].split('-')[1])+1))
    second_set =set(range(int(pair_list[1].split('-')[0]), int(pair_list[1].split('-')[1])+1))
    if(first_set.issubset(second_set) or set(first_set).issuperset(second_set)):
        subsets += 1

#Solution Part 1
print('Part one solution: ', subsets)

#Part 2

intersections = 0
for pair in pairs:
    pair_list = pair.split(',')
    first_set = set(range(int(pair_list[0].split('-')[0]), int(pair_list[0].split('-')[1])+1))
    second_set =set(range(int(pair_list[1].split('-')[0]), int(pair_list[1].split('-')[1])+1))
    if(first_set.intersection(second_set)):
        intersections += 1

#Solution Part 2
print('Part two solution: ', intersections)