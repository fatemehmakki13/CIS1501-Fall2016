import random

def print_board(board):
    for row in board:
        for number in row:
            for key, value in number.items():
                print(key, "-", value, end="\t")
        print()

def has_bingo(board):
    # checks each row for Bingo - assume has bingo until we find a false
    for row in board:
        rowHasBingo = True
        for number in row:
            for value in number.values():
                if not value:
                    rowHasBingo = False
        if rowHasBingo:
            return True

    # check each column for Bingo - assume has bingo until we find a false
    for col in range(len(board)):
        colHasBingo = True
        for row in board:
            for value in row[col].values():
                if not value:
                    colHasBingo = False
        if colHasBingo:
            return True

    #check diagonal top  left to bottom right
    topLeftToBottomRightHasBingo = True
    for index in range(len(board)):
        # make a new list of the values in the dictionary and get the first item ( index 0 )
        if not list(board[index][index].values())[0]:
            topLeftToBottomRightHasBingo = False
    if topLeftToBottomRightHasBingo:
        return True

    bottomLeftToTopRightHasBingo = True
    for index in range(len(board)):
        if not list(board[len(board) - 1 - index][index].values())[0]:
            bottomLeftToTopRightHasBingo = False
    if bottomLeftToTopRightHasBingo:
        return True

    return False

#fill list with numbers 1-65 to pick from
bingo_ball_tumbler = []
for number in range(1,66):
    bingo_ball_tumbler.append(number)

bingo_board = []
for row in range(5):
    bingo_board.append([])
    for col in range(5):
        random_number = random.randint(1,65)
        # has the random number already been picked?
        if random_number in bingo_ball_tumbler:
            bingo_board[row].append( { random_number : False } )
            bingo_ball_tumbler.remove(random_number)

print_board(bingo_board)

while(not has_bingo(bingo_board) ):
    bingoBall = int(input( "Please enter a number 1-65: " ))
    for row in bingo_board:
        for number in row:
            if bingoBall in number:
                number[bingoBall] = True

print_board(bingo_board)