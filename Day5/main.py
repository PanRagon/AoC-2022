from input import input, crates

moves = input.split('\n')
#Part 1
def part1():
    crates_first = crates
    for move in moves:
        move = move.split()
        del move[::2]
        move = list(map(int, move))
        for i in range(0, move[0]):
            crate = crates_first[move[1]-1].pop(0)
            crates_first[move[2]-1].insert(0, crate)
        
    res = ""
    for crate in crates_first:
        res += crate[0]
    print('Solution Part 1: ', res)
#Solve Part 1
part1()

#Part 2
def part2():
    crates_second = crates
    for move in moves:
        move = move.split()
        del move[::2]
        move = list(map(int, move))
        crate_stack = crates_second[move[1]-1][0:move[0]]
        del crates_second[move[1]-1][0:move[0]]
        crates_second[move[2]-1] = crate_stack + crates_second[move[2]-1]
    res = ""
    for crate in crates_second:
        if(len(crate) > 0):
            res += crate[0] or ''
    print('Solution Part 2: ', res)

#Solve Part 2
part2()