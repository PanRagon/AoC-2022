from test import test_input

grid = test_input.split()
for idx, row in enumerate(grid):
    grid[idx] = list(row)

def find_and_replace_grid(start_char, end_char, grid):
    start = (0,0)
    end = (0,0)
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == start_char:
                start = (x, y)
                grid[x][y] = 'a'
            if col == end_char:
                end = (x, y)
                grid[x][y] = 'z'
    return (start, end, grid)

def find_bfs_path(grid):
    start, end, grid = find_and_replace_grid('S', 'E', grid)
    print(get_neighbors(start, grid))

def get_neighbors(node, grid):
    x, y = node
    neighbors = []
    print(compare_neighbor(grid[x][y], grid[x - 1][y]))
    if x > 0 and compare_neighbor(grid[x][y], grid[x - 1][y]):
        neighbors.append((x - 1, y))
    if x < len(grid) - 1 and compare_neighbor(grid[x][y], grid[x + 1][y]):
        neighbors.append((x + 1, y))
    if y > 0 and compare_neighbor(grid[x][y], grid[x][y - 1]):
        neighbors.append((x, y - 1))
    if y < len(grid[0]) - 1 and compare_neighbor(grid[x][y], grid[x][y + 1]):
        neighbors.append((x, y + 1))
    return neighbors

def compare_neighbor(curr, compare):
    return ord(compare) in range(0, ord(curr) + 1)


find_bfs_path(grid)