def create_board():
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'W', 'B', '.', '.', '.'],
            ['.', '.', '.', 'B', 'W', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.']]
    list_alp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in list_alp:
        print(i, end=' ')
    print('')
    start = 1
    for i in board:
        print(start, end=' ')
        start += 1
        for j in i:
            print (j, end=' ')
        print('')
    return board

"""---Create the board---"""


def next_cells(y, x):
    board = create_board()
    list = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
    next_cell = []
    for dy, dx in list:
        pair = [y+dy,x+dx]
        next_cell.append(pair)
    return next_cell
print(next_cells(4,3))
"""---Return a list of next cells---"""
