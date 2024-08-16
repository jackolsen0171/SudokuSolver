#== TO 

import pygame 
pygame.init()


WIDTH, HEIGHT = (504, 504)
rowsCols = 9

WHITE = (255,255,255)
BLACK = (0,0,0)
CELL_SIZE = WIDTH // rowsCols

win = pygame.display.set_mode((504,504))
pygame.display.set_caption('Sudoku Solver')
clock = pygame.time.Clock()

timerEvent = pygame.USEREVENT

pygame.time.set_timer(timerEvent,1000)#timer
font = pygame.font.SysFont('Consolas', 30)


board =[['5', '3', '.', '.', '7', '.', '.', '.', '.'], 
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

        
    
def printBoard(board):
    for row in board:
        print(row)

def findEmpty():
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    return i,j
                
        else:
            return False

def possible(row,col,num):
        # Check num doesnt exists in current cells row or column
        for i in range(len(board)):
            if board[row][i] == num or board[i][col] == num:
                return False
            
        miniGridRow = ((row//3) + 1) * 3 - 3
        miniGridCol = ((col//3) + 1) * 3 - 3
        
        for i in range(3):
            for j in range(3):
                if board[miniGridRow+i][miniGridCol+j] == num:
                    return False
        
        return True
    
def solve(board):
    
        empty = findEmpty()
        if empty == False:
            return True
        
        else:
            i,j = empty
        for number in range(1,10):
            if possible(i,j,str(number)):
                board[i][j] = str(number)
                draw(win, board)
                 # Solve returns false if next number not possible or no empties. In that case the board is solved
                if solve(board) == False:
                    # This states current number leads to a wrong solution so dont place the number
                    board[i][j] = '.'
                    draw(win, board)
                else:
                    # number is in its correct spot
                    return True
            
        return False


##########################################

def draw_grid(win, grid):
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            pygame.draw.rect(win, WHITE, ((j * CELL_SIZE),(i * CELL_SIZE), CELL_SIZE, CELL_SIZE))
            surface = font.render(str(num), False, (0,0,0))
            win.blit(surface, ((j * CELL_SIZE)+15,(i * CELL_SIZE)+15))

    thickness = 1

    for i in range(rowsCols):
        if i % 3 == 0: thickness = 3
        pygame.draw.line(win, BLACK,((i * CELL_SIZE),0),(i * CELL_SIZE,HEIGHT), thickness )
        pygame.draw.line(win, BLACK, (0, (i * CELL_SIZE)), (WIDTH, i * CELL_SIZE), thickness)
        thickness = 1
    # pygame.draw.line(win, BLACK, (202, 0),(202, 504))

def draw(win, board):
     win.fill(WHITE)
     draw_grid(win, board)
     pygame.display.update()
        
def gameLoop():
    run = True
    keys = pygame.key.get_pressed()
    while run:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(board)

            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        draw(win, board)
        clock.tick(30)

    pygame.quit()

gameLoop()