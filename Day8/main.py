from input import input
from test import test_input


#Init
def parse_input(input):
    rows = input.split()
    grid = []
    for row in rows:
        row_list = []
        for char in row:
            row_list.append(int(char))
        grid.append(row_list)
    return grid

def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end='')
        print()

grid = parse_input(input)
print_grid(grid)

#Part 1
def count_visible(grid):
    count = 0
    for outer_idx, row in enumerate(grid):
        for inner_idx, tree in enumerate(row):
            if(outer_idx == 0 or outer_idx == len(grid) - 1):
                count+=1
            elif(inner_idx == 0 or inner_idx == len(row) - 1):
                count += 1
            else:
                #Check above
                visible = True
                for i in range(0, outer_idx):
                    if(grid[i][inner_idx] >= tree):
                        visible = False
                if(visible):
                    count+=1
                    continue
                #Check left
                visible = True
                for i in range(0, inner_idx):
                    if(grid[outer_idx][i] >= tree):
                        visible = False
                if(visible):
                    count+=1
                    continue
                #Check right
                visible = True
                for i in range(inner_idx + 1, len(row)):
                    if(grid[outer_idx][i] >= tree):
                        visible = False
                if(visible):
                    count+=1
                    continue   
                #Check below
                visible = True
                for i in range(outer_idx + 1, len(grid)):
                    if(grid[i][inner_idx] >= tree):
                        visible = False
                if(visible):
                    count+=1
    return count

#Part 1 Solution
p1_result = count_visible(grid)
print('Part 1 Solution: ', p1_result)

#Part 2
def highest_scenic_score(grid):
    highest_score = 0
    for outer_idx, row in enumerate(grid):
        for inner_idx, tree in enumerate(row):
            above = 0
            left = 0
            right = 0
            below = 0
            #Count above
            for i in range(outer_idx-1, -1, -1):
                above += 1
                if(grid[i][inner_idx] >= tree):
                    break
            #Count left
            for i in range(inner_idx-1, -1, -1):
                left += 1
                if(grid[outer_idx][i] >= tree):
                    break
            #Count right
            for i in range(inner_idx + 1, len(row)):
                right += 1   
                if(grid[outer_idx][i] >= tree):
                    break
            #Count below
            for i in range(outer_idx + 1, len(grid)):
                below += 1
                if(grid[i][inner_idx] >= tree):
                    break
            score = above * left * right * below
            if(score > highest_score):
                highest_score = score
    return highest_score

#Part 2 Solution
p2_result = highest_scenic_score(grid)
print("Part 2 Solution: ", p2_result)