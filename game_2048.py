from random import randint
from copy import deepcopy
import pyfiglet

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


def rotate90(grid):
    rotatedgrid = deepcopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            rotatedgrid[i][j] = grid[-(j + 1)][i]
    return rotatedgrid


def rotate90back(grid):
    rotatedbackgrid = deepcopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            rotatedbackgrid[-(j + 1)][i] = grid[i][j]
    return rotatedbackgrid


def move_cells(grid):
    """Function to move cells"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (
                grid[i][j] != 0 and i != 0
            ):  # only enter while loop if filled and not already in utmost row/column
                row = i
                going = True
                while going:
                    row -= 1
                    if grid[row][j] == grid[i][j]:
                        grid[row][j] += grid[i][j]
                        grid[i][j] = 0
                        going = False
                    elif grid[row][j] == 0 and row != 0:
                        going = True
                    elif grid[row][j] == 0 and row == 0:
                        grid[row][j] = grid[i][j]
                        grid[i][j] = 0
                        going = False
                    elif grid[row][j] != grid[i][j]:
                        grid[row + 1][j] = grid[i][j]
                        if not (row + 1) == i:
                            grid[i][j] = 0
                        going = False
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
    match direction:
        case "left":
            grid = rotate90(grid)
        case "right":
            grid = rotate90back(grid)
        case "down":
            grid1 = rotate90(grid)
            grid = rotate90(grid1)
    grid = move_cells(grid)
    grid = fill_new_cell(grid)

    match direction:
        case "left":
            grid = rotate90back(grid)
        case "right":
            grid = rotate90(grid)
        case "down":
            grid1 = rotate90(grid)
            grid = rotate90(grid1)

    print(*grid, sep="\n")
    print("\n")
    return grid


def game_loop(grid):
    """Main game loop"""
    while True:
        press = input(
            "Press w for up, s for down, a for left, d for right, q to quit: "
        )
        match press:
            case "w":
                grid = swipe(grid, "up")
            case "s":
                grid = swipe(grid, "down")
            case "a":
                grid = swipe(grid, "left")
            case "d":
                grid = swipe(grid, "right")
            case "q":
                break


if __name__ == "__main__":
    welcome = pyfiglet.figlet_format("Welcome to 2048", font="slant")
    print(welcome)
    grid = initialize_grid()
    print(*grid, sep="\n")
    print("\n")
    game_loop(grid)

    # # fortesting simulate a bunch of swipes
    # i = 0
    # while i < 10:
    #     grid = swipe(grid, "down")
    #     i += 1
