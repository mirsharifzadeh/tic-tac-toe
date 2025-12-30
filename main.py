import pygame
from funcs import *

GRID_SIZE = 3
ROWS = [26, 226, 426]
COLS = [30, 230, 430]

grid = [['' for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

pygame.init()

width = 600
height = 600
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("TIC-TAC-TOE")

board = pygame.image.load("images/board.png")
board_coord = board.get_rect()

X = pygame.image.load("images/xxx.png")
X = pygame.transform.scale(X, (150, 150))
X_coord = X.get_rect()
X_coord.topleft = (26, 30)

O = pygame.image.load("images/ooo.png")
O = pygame.transform.smoothscale(O, (150, 150))
O_coord = O.get_rect()
O_coord.topleft = (226, 230)

font = pygame.font.SysFont('consolas', 72)
text_x = font.render("X WINS!", True, (255, 255, 255))
text_x_coord = text_x.get_rect()
text_x_coord.center = (300, 300)

text_o = font.render("O WINS!", True, (255, 255, 255))
text_o_coord = text_o.get_rect()
text_o_coord.center = (300, 300)

text_draw = font.render("DRAW!", True, (255, 255, 255))
text_draw_coord = text_draw.get_rect()
text_draw_coord.center = (300, 300)

window_bool = True
turn = 'X'
coords_x = []
coords_o = []

while window_bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_bool = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_bool = False

        if not (check_row_x(grid) or check_row_o(grid) or check_col_x(grid) or check_col_o(grid) or check_cross_x(grid) or check_cross_o(grid) or check_cells(grid)):
            if turn == 'X':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    if mouse_x in range(0, 191) and mouse_y in range(0, 191):
                        if coords_x.count((ROWS[0], COLS[0])) == 0:
                            coords_x.append((ROWS[0], COLS[0]))
                            grid[0][0] = 'X'
                            turn = 'O'
                    elif mouse_x in range(0, 191) and mouse_y in range(220, 381):
                        if coords_x.count((ROWS[0], COLS[1])) == 0:
                            coords_x.append((ROWS[0], COLS[1]))
                            grid[1][0] = 'X'
                            turn = 'O'
                    elif mouse_x in range(0, 191) and mouse_y in range(410, 601):
                        if coords_x.count((ROWS[0], COLS[2])) == 0:
                            coords_x.append((ROWS[0], COLS[2]))
                            grid[2][0] = 'X'
                            turn = 'O'
                    elif mouse_x in range(220, 381) and mouse_y in range(0, 191):
                        if coords_x.count((ROWS[1], COLS[0])) == 0:
                            coords_x.append((ROWS[1], COLS[0]))
                            grid[0][1] = 'X'
                            turn = 'O'
                    elif mouse_x in range(220, 381) and mouse_y in range(225, 384):
                        if coords_x.count((ROWS[1], COLS[1])) == 0:
                            coords_x.append((ROWS[1], COLS[1]))
                            grid[1][1] = 'X'
                            turn = 'O'
                    elif mouse_x in range(220, 381) and mouse_y in range(415, 601):
                        if coords_x.count((ROWS[1], COLS[2])) == 0:
                            coords_x.append((ROWS[1], COLS[2]))
                            grid[2][1] = 'X'
                            turn = 'O'
                    elif mouse_x in range(410, 601) and mouse_y in range(0, 191):
                        if coords_x.count((ROWS[2], COLS[0])) == 0:
                            coords_x.append((ROWS[2], COLS[0]))
                            grid[0][2] = 'X'
                            turn = 'O'
                    elif mouse_x in range(410, 601) and mouse_y in range(225, 384):
                        if coords_x.count((ROWS[2], COLS[1])) == 0:
                            coords_x.append((ROWS[2], COLS[1]))
                            grid[1][2] = 'X'
                            turn = 'O'
                    elif mouse_x in range(410, 601) and mouse_y in range(415, 601):
                        if coords_x.count((ROWS[2], COLS[2])) == 0:
                            coords_x.append((ROWS[2], COLS[2]))
                            grid[2][2] = 'X'
                            turn = 'O'
                    for i in grid:
                        print(i)
            elif turn == 'O':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    if mouse_x in range(0, 191) and mouse_y in range(0, 191):
                        if coords_o.count((ROWS[0], COLS[0])) == 0:
                            coords_o.append((ROWS[0], COLS[0]))
                            grid[0][0] = 'O'
                            turn = 'X'
                    elif mouse_x in range(0, 191) and mouse_y in range(220, 381):
                        if coords_o.count((ROWS[0], COLS[1])) == 0:
                            coords_o.append((ROWS[0], COLS[1]))
                            grid[1][0] = 'O'
                            turn = 'X'
                    elif mouse_x in range(0, 191) and mouse_y in range(410, 601):
                        if coords_o.count((ROWS[0], COLS[2])) == 0:
                            coords_o.append((ROWS[0], COLS[2]))
                            grid[2][0] = 'O'
                            turn = 'X'
                    elif mouse_x in range(220, 381) and mouse_y in range(0, 191):
                        if coords_o.count((ROWS[1], COLS[0])) == 0:
                            coords_o.append((ROWS[1], COLS[0]))
                            grid[0][1] = 'O'
                            turn = 'X'
                    elif mouse_x in range(220, 381) and mouse_y in range(225, 384):
                        if coords_o.count((ROWS[1], COLS[1])) == 0:
                            coords_o.append((ROWS[1], COLS[1]))
                            grid[1][1] = 'O'
                            turn = 'X'
                    elif mouse_x in range(220, 381) and mouse_y in range(415, 601):
                        if coords_o.count((ROWS[1], COLS[2])) == 0:
                            coords_o.append((ROWS[1], COLS[2]))
                            grid[2][1] = 'O'
                            turn = 'X'
                    elif mouse_x in range(410, 601) and mouse_y in range(0, 191):
                        if coords_o.count((ROWS[2], COLS[0])) == 0:
                            coords_o.append((ROWS[2], COLS[0]))
                            grid[0][2] = 'O'
                            turn = 'X'
                    elif mouse_x in range(410, 601) and mouse_y in range(225, 384):
                        if coords_o.count((ROWS[2], COLS[1])) == 0:
                            coords_o.append((ROWS[2], COLS[1]))
                            grid[1][2] = 'O'
                            turn = 'X'
                    elif mouse_x in range(410, 601) and mouse_y in range(415, 601):
                        if coords_o.count((ROWS[2], COLS[2])) == 0:
                            coords_o.append((ROWS[2], COLS[2]))
                            grid[2][2] = 'O'
                            turn = 'X'

                    print("X: {} Y: {}".format(mouse_x, mouse_y))

                    for i in grid:
                        print(i)

    if not (check_row_x(grid) or check_row_o(grid) or check_col_x(grid) or check_col_o(grid) or check_cross_x(grid) or check_cross_o(grid) or check_cells(grid)):
        window.fill((255, 255, 255))
        for i in coords_x:
            window.blit(X, i)
        for j in coords_o:
            window.blit(O, j)
        window.blit(board, board_coord)

    elif check_cells(grid) and not(check_row_x(grid) or check_row_o(grid) or check_col_x(grid) or check_col_o(grid) or check_cross_x(grid) or check_cross_o(grid)):
        window.fill((0, 0, 0))
        window.blit(text_draw, text_draw_coord)

    else:
        window.fill((0, 0, 0))
        if check_cross_x(grid) or check_col_x(grid) or check_row_x(grid):
            window.blit(text_x, text_x_coord)
        elif check_cross_o(grid) or check_col_o(grid) or check_row_o(grid):
            window.blit(text_o, text_o_coord)

    pygame.display.update()

pygame.quit()