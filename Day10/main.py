import math
from test import test_input
from input import input

#Setup
instructions = input.split('\n')
def execute_instruction(instruction):
    instruction = instruction.split()
    #Returns an array with the number of steps to execute, and the number to increment state by
    if(instruction[0] == "noop"):
        return [1, 0]
    else:
        return [2, int(instruction[1])]

#Part 1 & 2
def draw_grid(instructions, terminal_width):
    cycles = 0
    register = 1
    grid = [[],[],[],[],[],[]]
    signal_result = 0
    for instruction in instructions:
        steps = execute_instruction(instruction)
        for i in range(steps[0]):
            draw_range = range(register-1, register+2)
            grid[math.floor(cycles/terminal_width)].append('#' if cycles % terminal_width in draw_range else '.')
            cycles += 1
            if(cycles % terminal_width == terminal_width / 2):
                signal_result += register * cycles
        register += steps[1]
    print('Solution to part 1: ', signal_result)
    return grid

def print_grid(grid):
    print('Solution to part 2: ')
    for row in grid:
        for cell in row:
            if(cell == '#'):
                print(u'\u2588\u2588', end="")
            else: print(u'\u2591\u2591', end="")
        print('')

#Part 2 Solution
grid = draw_grid(instructions, 40)
print_grid(grid)