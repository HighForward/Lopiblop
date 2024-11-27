def getDoubleIndex(grid, i):
    tmp = 0
    while tmp < i:
        if grid[tmp].blop and grid[i].blop and grid[tmp].blop.name == grid[i].blop.name:
            return tmp
        tmp += 1
    return -1