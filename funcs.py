def check_cells(grd):
    m = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if grd[i][j]:
                m += 1
    if m >= 9:
        return True

    return False

def check_row_x(grd):

    for i in range(0, 3):
        m = 0
        for j in range(0, 3):
            if grd[i][j] == 'X':
                m += 1

        if m == 3:
            return True

    return False

def check_row_o(grd):

    for i in range(0, 3):
        m = 0
        for j in range(0, 3):
            if grd[i][j] == 'O':
                m += 1

        if m == 3:
            return True

    return False

def check_col_x(grd):

    for i in range(0, 3):
        m = 0
        for j in range(0, 3):
            if grd[j][i] == 'X':
                m += 1

        if m == 3:
            return True

    return False

def check_col_o(grd):

    for i in range(0, 3):
        m = 0
        for j in range(0, 3):
            if grd[j][i] == 'O':
                m += 1

        if m == 3:
            return True

    return False

def check_cross_x(grd):
    m = 0
    for i in range(0, 3):
        if grd[i][i] == 'X':
            m += 1
    if m == 3:
        return True

    m = 0
    for i in range(3):
        if grd[i][2 - i] == 'X':
            m += 1
    if m == 3:
        return True

    return False

def check_cross_o(grd):
    m = 0
    for i in range(0, 3):
        if grd[i][i] == 'O':
            m += 1
    if m == 3:
        return True

    m = 0
    for i in range(3):
        if grd[i][2 - i] == 'O':
            m += 1
    if m == 3:
        return True

    return False

GRID_SIZE = 3

grid = [['' for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

for i in grid:
    print(i)

if check_cross_x(grid):
    print("X WINS!")

