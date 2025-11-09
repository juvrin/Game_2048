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


def loop_up_down(i, grid, direction, constant):
    """Function to loop up and down"""
    for j in range(len(grid[i])):
        if (
            grid[i][j] != 0 and i != constant
        ):  # only enter while loop if filled and not already on top/bottom row
            row = i
            going = True
            while going:
                if direction == "up":
                    row -= 1
                else:
                    row += 1
                if grid[row][j] == grid[i][j]:
                    grid[row][j] += grid[i][j]
                    grid[i][j] = 0
                    going = False
                elif grid[row][j] == 0 and row != constant:
                    going = True
                elif grid[row][j] == 0 and row == constant:
                    grid[row][j] = grid[i][j]
                    grid[i][j] = 0
                    going = False
                elif grid[row][j] != grid[i][j]:
                    if direction == "up":
                        grid[row + 1][j] = grid[i][j]
                        if not (row + 1) == i:
                            grid[i][j] = 0
                    if direction == "down":
                        grid[row - 1][j] = grid[i][j]
                        if not (row - 1) == i:
                            grid[i][j] = 0
                    going = False
    return grid


# MOETNOG dit werkt nog niet
def loop_left(grid, direction, constant):
    """Function to loop left and right"""
    j = 0
    while j < len(grid[0]):
        for i in grid:
            if (
                i[j] != 0 and j != constant
            ):  # only enter while loop if filled and not already in utmost left/right column
                col = j
                going = True
                while going:
                    if direction == "left":
                        col -= 1
                    else:
                        col += 1
                    if i[col] == i[j]:
                        i[col] += i[j]
                        i[j] = 0
                        going = False
                    elif i[col] == 0 and col != constant:
                        going = True
                    elif i[col] == 0 and col == constant:
                        i[col] = i[j]
                        i[j] = 0
                        going = False
                    elif i[col] != i[j]:
                        if direction == "left":
                            i[col + 1] = i[j]
                            if not (col + 1) == j:
                                i[j] = 0
                        if direction == "right":
                            i[col - 1] = i[j]
                            if not (col - 1) == j:
                                i[j] = 0
                        going = False
            j += 1

    return grid


def move_cells(grid, direction):
    if direction == "up":
        constant = 0
        for i in range(len(grid)):
            loop_up_down(i, grid, direction, constant)
    if direction == "down":
        constant = 3
        for i in range(len(grid) - 1, -1, -1):
            loop_up_down(i, grid, direction, constant)
    if direction == "left":
        constant = 0
        loop_left(grid, direction, constant)
    if direction == "right":
        constant = 3
        # dit is hoe je dan moet loopen: steeds over het laatste element van de versch lijsten binnen grid
        # dan naar het tweede element etc
        # grid[0][3] => grid [1][3] => grid[2][3] => grid[3][3] => grid[0][2] => grid[1][2] etc
        # for i in range zorgen dat je looped van R kolom eerst naar L kolommen
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


def swipe(grid, direction):
    """Combine above functions into one swipe process"""
    grid = move_cells(grid, direction)
    grid = fill_new_cell(grid)
    print("\n======= Grid after swipe =======")
    print_grid(grid)


if __name__ == "__main__":
    grid = initialize_grid()
    print("\n======= Grid after setup =======")
    print_grid(grid)

    # fortesting simulate a bunch of swipes
    i = 0
    while i < 10:
        swipe(grid, "left")
        i += 1
