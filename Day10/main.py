import math
from test_input import test_input
from input import input

#Setup

instructions = input.split('\n')
#Part 1
def execute_instruction(instruction):
    instruction = instruction.split()
    #Returns an array with the number of steps to execute, and the number to increment state by
    if(instruction[0] == "noop"):
        return [1, 0]
    else:
        return [2, int(instruction[1])]

def calculate_signal(instructions, poi):
    cycles = 0
    register = 1
    result = 0
    for instruction in instructions:
        steps = execute_instruction(instruction)
        for i in range(steps[0]):
            cycles += 1
            if(cycles in poi):
                result += register * cycles
        register += steps[1]
    return result

#Part 1 Solution
resultp1 = calculate_signal(instructions, [20, 60, 100, 140, 180, 220])
print('Result of part 1: ', resultp1)

#Part 2

def draw_grid(instructions):
    cycles = 0
    register = 1
    grid = [[],[],[],[],[],[]]
    for instruction in instructions:
        steps = execute_instruction(instruction)
        for i in range(steps[0]):
            draw_range = range(register-1, register+2)
            grid[math.floor(cycles/40)].append('#' if cycles % 40 in draw_range else '.')
            cycles += 1
        register += steps[1]
    return grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            if(cell == '#'):
                print(u'\u2588\u2588', end="")
            else: print(u'\u2591\u2591', end="")
        print('')

#Part 2 Solution
grid = draw_grid(instructions)
print_grid(grid)