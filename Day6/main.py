from input import input

#Part 1
def main(distinct_length):
    start = 0
    for idx, first_marker in enumerate(input):
        if(start > 0):
            break
        chars = [first_marker]
        for second_marker in input[idx+1:]:
            if(second_marker not in chars):
                chars.append(second_marker)
                if(len(chars) == distinct_length):
                    print(chars)
                    start = idx+distinct_length
                    break
            else:
                break
    return start
print('Solution Part 1: ', main(4))
print('Solution Part 2: ', main(14))