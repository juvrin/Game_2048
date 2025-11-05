from random import randint


def initialize_grid():
    """Initialize playing grid before playing"""
    """ as a reference
    1 | 2 | 3 | 4 |
    5 | 6 | 7 | 8 |
    9 | 10| 11| 12|
    13| 14| 15| 16|
    """

    # fill two random cells with 2's
    rand1 = randint(1, 16)
    rand2 = randint(1, 16)

    # initiate grid
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # replace blank space with '2' for the randomly selected cells
    cor1 = ((rand1 - 1) // 4), ((rand1 - 1) % 4)
    cor2 = ((rand2 - 1) // 4), ((rand2 - 1) % 4)
    grid[cor1[0]][cor1[1]] = 2
    grid[cor2[0]][cor2[1]] = 2
    return grid


def print_grid(grid):
    """Print the grid with one list per line"""
    print(*grid, sep="\n")


def retrieve_filled_cells(grid):
    """Retrieve coordinates of filled cells as a list of tuples"""
    filledcells = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                filledcells.append((i, j))
    return filledcells


def swipe_up(filledcells, grid):
    """Move filledcells to new position. There are 3 possible scenarios:
    1) if there is a cell above them that is filled and it's the same number => addition
    2) if there is a cell above them that is filled and it's NOT the same number => it stays put
    3) if the cell above is empty/filled with 0, we keep going up until either
    scenario 1 or 2 occurs OR we're at the top row (row == 0)
    """
    for fc in filledcells:
        if fc[0] != 0:  # only enter while loop if not already on top row
            row = fc[0]
            goingup = True
            while goingup:
                row -= 1
                if grid[row][fc[1]] == grid[fc[0]][fc[1]]:
                    grid[row][fc[1]] += grid[fc[0]][fc[1]]
                    grid[fc[0]][fc[1]] = 0
                    goingup = False
                elif grid[row][fc[1]] != grid[fc[0]][fc[1]] and grid[row][fc[1]] != 0:
                    goingup = False
                elif grid[row][fc[1]] == 0 and row != 0:
                    continue
                elif row == 0:
                    grid[row][fc[1]] = grid[fc[0]][fc[1]]
                    grid[fc[0]][fc[1]] = 0
                    goingup = False
    return grid


def fill_new_cell(grid):
    """An empty cell is randomly selected and filled with 2"""
    randcorpool = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                randcorpool.append((i, j))
    cornew = randcorpool[randint(1, len(randcorpool))]
    grid[cornew[0]][cornew[1]] = 2
    return grid


if __name__ == "__main__":
    grid = initialize_grid()
    print("\n======= Grid after setup =======")
    print_grid(grid)
    filledcells = retrieve_filled_cells(grid)
    grid = swipe_up(filledcells, grid)
    grid = fill_new_cell(grid)
    print("\n======= Grid after swipe up =======")
    print_grid(grid)
