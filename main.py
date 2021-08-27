import random
import pygame

WIDTH = 700
HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
board = [
         [7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

pygame.init()
NUMBER_FONT = pygame.font.SysFont('courier', 25)

def draw_board(win, board):
    run = True
    pygame.draw.rect(win, BLACK, (5, 5, 490, 490), 4)

    for i in range(0,9):
        if (i+1) % 3 == 0:
            thickness = 4
        else:
            thickness = 2
        pygame.draw.lines(win, BLACK, False, [((i+1)*55, 5), ((i+1)*55, 495)], thickness)
        pygame.draw.lines(win, BLACK, False, [(5, (i+1)*55), (495, (i+1)*55)], thickness)
        for j in range(0,9):
            text = NUMBER_FONT.render(str(board[j][i]), 1, BLACK)
            win.blit(text, (((i+1)*55- text.get_width() / 2)-25, ((j+1)*55 - text.get_height() / 2)-25))
        pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                print(m_x // 55, m_y // 55)

def valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[j][i] == num and (j,i) != pos:
                return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[j][i] == 0:
                return (j,i)
    return None

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0
    return False

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((WHITE))
pygame.display.set_caption("Sudoku Game")
pygame.display.update()
solve(board)
draw_board(win, board)
pygame.display.update()

