def create_board():
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list = [list1, list2, list3, list4, list5, list6, list7, list8]
    for i in list:
        for j in range(8):
            i.append('.')
    board = [list1, list2, list3, list4, list5, list6, list7, list8]
    board[3][3], board[3][4] = "W", "B"
    board[4][3], board[4][4] = "B", "W"
    #print the first line
    print('  a b c d e f g h')
    #print the numbers and the dots list by list in board
    start = 1
    for i in board:
        print(start, end=' ')
        start += 1
        for j in i:
            print (j, end=' ')
        #newline after printing all the dots in the list
        print('')

"""              Create the board          """


def check_horiz_left(y, x):
    if x - 1 < 0:
        return False
    if board[y][x - 1] == '.':
        return False
    elif board[y][x - 1] == board[y][x]:
        return False
    else:
        for i in range(2, x + 1):
            if board[y][x - i] == '.':
                return True
            elif board[y][x - i] == board[y][x]:
                return False
        return False


def check_horiz_right(y, x):
    if x + 1 > 7:
        return False
    if board[y][x + 1] == '.':
        return False
    elif board[y][x + 1] == board[y][x]:
        return False
    else:
        for i in range(2, 8 - y):
            if board[y][x + i] == '.':
                return True
            elif board[y][x + i] == board[y][x]:
                return False
        return False

"""           Check horizontal          """


def check_verti_top(y,x):
    if y - 1 < 0:
        return False
    if board[y - 1][x] == '.':
        return False
    elif board[y - 1][x] == board[y][x]:
        return False
    else:
        for i in range(2, y + 1):
            if board[y - i][x] == '.':
                return True
            elif board[y - i][x] == board[y][x]:
                return False
        return False


def check_verti_bot(y,x):
    if y + 1 > 7:
        return False
    if board[y + 1][x] == '.':
        return False
    elif board[y + 1][x] == board[y][x]:
        return False
    else:
        for i in range(2, 8 - y):
            if board[y - i][x] == '.':
                return True
            elif board[y - i][x] == board[y][x]:
                return False
        return False

"""              Check vertical          """


def check_diago_topleft(y,x):
    if y - 1 < 0 or x - 1 < 0:
        return False
    if board[y - 1][x - 1] == '.':
        return False
    elif board[y - 1][x - 1] == board[y][x]:
        return False
    else:
        z = x
        if y < x:
            z = y
        for i in range(2, z + 1):
            if board[y - i][x - i] == '.':
                return True
            elif board[y - i][x - i] == board[y][x]:
                return False
        return False


def check_diago_botright(y,x):
    if y + 1 > 7 or x + 1 > 7:
        return False
    if board[y + 1][x + 1] == '.':
        return False
    elif board[y + 1][x + 1] == board[y][x]:
        return False
    else:
        z = x
        if y > x:
            z = y
        for i in range(2, 8 - z):
            if board[y + i][x + i] == '.':
                return True
            elif board[y + i][x + i] == board[y][x]:
                return False
        return False
