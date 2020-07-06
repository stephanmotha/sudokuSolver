from typing import List, Tuple, Optional


# sample board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],

    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],

    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(bo: List[List]) -> None:
    # iterate through rows
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - ')

        # iterate through columns
        for j in range(len(bo[i])):
            # add line and space every 3
            if j % 3 == 0:
                print('|' + ' ', end='')

            print(str(bo[i][j]) + ' ', end='')

            # don't print the next on the same line if it is the last in the row
            if j+1 == len(bo[i]):
                print('|')


# picks an empty position in the grid
def pick_empty(bo: List[List]) -> Optional[Tuple]:
    # iterate through rows
    for row in range(len(bo)):
        # iterate through columns
        for col in range(len(bo[row])):
            # if you find empty space, return the position
            if bo[row][col] == 0:
                return row, col  # row, col

    return None


# checks 1. the row 2. the column 3. the 3 x 3 grid to see if num is valid
def valid_board(bo: List[List], num: int, pos: tuple) -> bool:

    # check row and column
    for i in range(len(bo)):
        if (bo[pos[0]][i] == num) or (bo[i][pos[1]] == num):
            return False

    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col*3, box_col * 3 + 3):
            if bo[i][j] == num:
                return False

    return True


def solve(bo: List[List]) -> bool:

    found = pick_empty(bo)

    # return True if no 0 left -> solution found
    if not found:
        return True

    else:
        row, col = found

        # try numbers 1-9 in the board
        for i in range(1, 10):
            # if number is valid, put it in
            if valid_board(bo, i, (row, col)):
                bo[row][col] = i

                # recursively call solve on the new board with the new num added
                if solve(bo):
                    return True


                bo[row][col] = 0

    # if no num works, reset the prev num to 0 and continue the for loop outside
    # of the recursion (the prev found slot). this means the for loop does not
    # reset

    return False


print_board(board)
solve(board)

print('\n')
print_board(board)




























