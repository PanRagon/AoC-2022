from test import test_input

grid = test_input.split()
for idx, row in enumerate(grid):
    grid[idx] = list(row)
print(grid)