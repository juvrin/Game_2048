from random import randint

""" as a reference
    1 | 2 | 3 | 4 |
    5 | 6 | 7 | 8 |
    9 | 10| 11| 12|
    13| 14| 15| 16|
    """


def initialize_grid():
    """Initialize playing grid before playing"""
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


"""Move filled cells to new position. There are 3 possible scenarios:
1) if there is a cell above them that is filled and it's the same number => addition
2) if there is a cell above them that is filled and it's NOT the same number => it stays put
3) if the cell above is empty/filled with 0, we keep going up until either
scenario 1 or 2 occurs OR we're at the top row (row == 0)
"""


def move_cells_up_down(grid, direction):
    if direction == "up":
        constant = 0
    if direction == "down":
        constant = 3

    # MOETNOG hier zorgen dat je van onder naar boven loopt indien
    # direction == "down"
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (
                grid[i][j] != 0 and i != constant
            ):  # only enter while loop if filled and not already on top/bottom row
                row = i
                goingup = True
                while goingup:
                    if direction == "up":
                        row -= 1
                    else:
                        row += 1
                    if grid[row][j] == grid[i][j]:
                        grid[row][j] += grid[i][j]
                        grid[i][j] = 0
                        goingup = False
                    elif grid[row][j] == 0 and row != constant:
                        goingup = True
                    elif grid[row][j] == 0 and row == constant:
                        grid[row][j] = grid[i][j]
                        grid[i][j] = 0
                        goingup = False
                    elif grid[row][j] != grid[i][j]:
                        if direction == "up":
                            grid[row + 1][j] = grid[i][j]
                            if not (row + 1) == i:
                                grid[i][j] = 0
                        if direction == "down":
                            grid[row - 1][j] = grid[i][j]
                            if not (row - 1) == i:
                                grid[i][j] = 0
                        goingup = False
    return grid


def move_filled_cells_right(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (
                grid[i][j] != 0 and j != 3
            ):  # only enter while loop if filled and not already in utmost right column
                col = j
                goingright = True
                while goingright:
                    col += 1
                    if grid[i][col] == grid[i][j]:
                        grid[i][col] += grid[i][j]
                        grid[i][j] = 0
                        goingright = False
                    elif grid[i][col] == 0 and col != 3:
                        goingright = True
                    elif grid[i][col] == 0 and col == 3:
                        grid[i][col] = grid[i][j]
                        grid[i][j] = 0
                        goingright = False
                    elif grid[i][col] != grid[i][j]:
                        grid[i][col - 1] = grid[i][j]
                        if not (col - 1) == j:
                            grid[i][j] = 0
                        goingright = False
    return grid


def fill_new_cell(grid):
    """An empty cell is randomly selected and filled with 2"""
    randcorpool = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                randcorpool.append((i, j))
    cornew = randcorpool[randint(0, len(randcorpool) - 1)]
    grid[cornew[0]][cornew[1]] = 2
    return grid


def swipe_up_down(grid, direction):
    """Combine above functions into one swipe up process"""
    grid = move_cells_up_down(grid, direction)
    grid = fill_new_cell(grid)
    print("\n======= Grid after swipe =======")
    print_grid(grid)


def swipe_right(grid):
    """Combine above functions into one swipe right process"""
    grid = move_filled_cells_right(grid)
    grid = fill_new_cell(grid)
    print("\n======= Grid after swipe =======")
    print_grid(grid)


if __name__ == "__main__":
    grid = initialize_grid()
    print("\n======= Grid after setup =======")
    print_grid(grid)

    # fortesting simulate a bunch of swipes
    i = 0
    while i < 20:
        swipe_up_down(grid, "down")
        i += 1
