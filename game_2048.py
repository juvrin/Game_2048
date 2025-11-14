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
    countmoves = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0 and i != 0 and grid[i][j] != "X":
                row = i
                going = True
                while going:
                    row -= 1
                    if grid[row][j] == grid[i][j]:
                        grid[row][j] += grid[i][j]
                        grid[row + 1][j] = "X"
                        if not (row + 1) == i:
                            grid[i][j] = 0
                            countmoves += 1
                        going = False
                    elif grid[row][j] == "X":
                        grid[row][j] = grid[i][j]
                        grid[i][j] = 0
                        countmoves += 1
                        going = False
                    elif grid[row][j] == 0 and row != 0:
                        going = True
                    elif grid[row][j] == 0 and row == 0:
                        grid[row][j] = grid[i][j]
                        grid[i][j] = 0
                        countmoves += 1
                        going = False
                    elif grid[row][j] != grid[i][j]:
                        grid[row + 1][j] = grid[i][j]
                        if not (row + 1) == i:
                            grid[i][j] = 0
                            countmoves += 1
                        going = False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                grid[i][j] = 0

    return grid, countmoves


def check_finished(grid, gameover, countmoves):
    """Check if game is finished"""
    countfill = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2048:
                gameover = True
            if grid[i][j] != 0:
                countfill += 1

    if countmoves == 0 and countfill == 16:
        gameover = True
    return gameover


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

    grid, countmoves = move_cells(grid)
    if countmoves > 0:
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
    return grid, countmoves


def game_loop(grid):
    """Main game loop"""
    gameover = False
    countgrids = 0
    while gameover == False:
        press = input(
            "Press w for up, s for down, a for left, d for right, q to quit: "
        )
        """
        # start fortesting
        options = ["w", "s", "a", "d"]
        randnum = randint(0, 3)
        press = options[randnum]
        # end fortesting
        """
        match press:
            case "w":
                grid, countmoves = swipe(grid, "up")
            case "s":
                grid, countmoves = swipe(grid, "down")
            case "a":
                grid, countmoves = swipe(grid, "left")
            case "d":
                grid, countmoves = swipe(grid, "right")
            case "q":
                break
        countgrids += 1
        gameover = check_finished(grid, gameover, countmoves)


if __name__ == "__main__":
    welcome = pyfiglet.figlet_format("Welcome to 2048", font="slant")
    print(welcome)
    grid = initialize_grid()
    print(*grid, sep="\n")
    print("\n")
    game_loop(grid)
    gameover = pyfiglet.figlet_format("Game over", font="slant")
    print(gameover)
