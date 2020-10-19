# slide puzzle 
# by shlomi 
# based on work of Al Sweigart 

import pygame, sys, random
from pygame.locals import *

# Create the constants
BOARDWIDTH = 6 # NUMBER OF COLUMNS IN THE BOARD
BOARDHEIGHT = 6  # NUMBER OF ROWS IN THE BOARD
TILESIZE = 80
WINDOWWIDTH = 740
WINDOWHEIGHT = 580
FPS = 60
BLANK = None

#        R G B
BLACK = (0,0,0)
WHITE = (255,255,255)
BRIGHTBLUE = (0,50,255)
DARKTURQUOISE = (0,50,255)
GREEN = (0,244,0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BOARDCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR =WHITE
BUTTONTEXTCOLOR =BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE *BOARDWIDTH +(BOARDWIDTH -1))) /2)
YMARGIN = int((WINDOWHEIGHT- (TILESIZE *BOARDHEIGHT+(BOARDHEIGHT -1))) /2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Slide puzzle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    direction = pygame.font.Font('freesansbold.ttf',BASICFONTSIZE)
    
    #store the option buttens and their rectangles in OPTIONS.
    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    NEW_SURF,NEW_RECT = makeText('New Game', TEXTCOLOR,TILECOLOR,WINDOWWIDTH -120,WINDOWHEIGHT-60)
    SOLVE_SURF,SOLVE_RECT = makeText('Solve', TEXTCOLOR,TILECOLOR,WINDOWWIDTH -120,WINDOWHEIGHT-30)
    
    mainBoard, solutionSeq = generateNewPuzzle(20) #start with 80 the higher -> the harder
    SOLVEBOARD =getStartingBoard() # solved board is the same as the board i the start
    
    allMoves = [] # list of moves made from the solved configuration
    # main game loop:
    while True:
        slideTo=None  #the dirction. if any, a tile should slide
        msg = '' #contains the message to show in upperleft corner
        
        if mainBoard == SOLVEBOARD:
            MSG= 'Solved!'
        
        drawBoard(mainBoard,msg)
        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard,event.pos[0],event.pos[1])
                
                if(spotx, spoty) == (None,None):
                    #check if the user cliked on option button
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) #clicked on Reset button
                        allMoves  = []
                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80) #clicked on new game button
                        allMoves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves) #clicked on Solve button
                        allMoves = []
                else: #check if the clicked tile was next to the blank spot
                        
                        
                    blankx,blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = LEFT
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky- 1:
                        slideTo = DOWN
            elif event.type == KEYUP:
                #check if the usr pressed a key to slidea a tile
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard,LEFT):
                    slideTo = LEFT
                if event.key in (K_RIGHT, K_d) and isValidMove(mainBoard,RIGHT):
                    slideTo = RIGHT
                if event.key in (K_UP, K_w) and isValidMove(mainBoard,UP):
                    slideTo = UP
                if event.key in (K_DOWN, K_s) and isValidMove(mainBoard,DOWN):
                    slideTo = DOWN
                    
            if slideTo:
                slideAnimation(mainBoard,slideTo,'click tile or press arrow keys to slide.',8) #show slide on screen
                makeMove(mainBoard, slideTo)
                allMoves.append(slideTo) # record th slide
            pygame.display.update()
            FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()
    
def checkForQuit():
    for event in pygame.event.get(QUIT):# get all the QUIT events
        terminate() # termanite if ant QUIT event present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if THE keyup was for  the Esc key
        pygame.event.post(event) # put the other KEYUP event object back

def getStartingBoard():
    # Return a board date structure with tiles in the solved state.
    # For exmple if BOARDWIDTH and BOARDHEIGHT are both 3, this function return
    #[[1,4,7],[2,5,8],[3,6,None]]
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH *(BOARDHEIGHT-1) +BOARDWIDTH -1
    
    board[BOARDWIDTH-1][BOARDHEIGHT-1] = None
    return board
    
def getBlankPosition(board):
    #return  x and y as board coordinate of the blank space
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == None:
                return (x,y)

def swap(a,b):
    return b,a
                
def makeMove(board,move):
    #This function does not check it move is valid.
    blankx, blanky = getBlankPosition(board)
    
    if move == UP:
        #board[blankx][blanky],board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
        board[blankx][blanky],board[blankx][blanky + 1] = swap(board[blankx][blanky],board[blankx][blanky + 1])
    elif move == DOWN:
        board[blankx][blanky],board[blankx][blanky - 1] = swap(board[blankx][blanky],board[blankx][blanky - 1]) 
    elif move == LEFT:
        board[blankx][blanky],board[blankx + 1][blanky] = swap(board[blankx][blanky],board[blankx + 1][blanky]) 
    elif move == RIGHT:
        board[blankx][blanky],board[blankx - 1][blanky] = swap(board[blankx][blanky],board[blankx - 1][blanky]) 
        
def isValidMove(board,move):
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) -1) or (move == DOWN and blanky != 0) or (move == LEFT and blankx != len(board) - 1) or (move == RIGHT and blankx != 0)
           
def getRandomMove(board,lastMove=None):
    #start with full list of four moves
    validMoves =[UP,DOWN,LEFT,RIGHT]
    #remove moves from the list as they are disqualified
    if lastMove == UP or not isValidMove(board,DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board,UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board,RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board,LEFT):
        validMoves.remove(LEFT)
    
    #return a random move from the list of remaining moves
    return random.choice(validMoves)
    
def getLeftTopOfTile(tileX,tileY):
    left = XMARGIN + (tileX * TILESIZE) +(tileX -1)
    top = YMARGIN +  (tileY * TILESIZE) +(tileY -1)  
    return (left,top)

def getSpotClicked(board, x, y):
    #from x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX,tileY)
            tileRect =pygame.Rect(left,top,TILESIZE,TILESIZE)
            if tileRect.collidepoint(x,y):
                return(tileX,tileY)
    return(None,None)
    
def drawTile(tilex,tiley, number, adjx = 0, adjy = 0):
    #darw a tile at board coordinate tilex and tailey optionally a few pixels over (determined by asjx and adjy)
    left, top =getLeftTopOfTile(tilex,tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))     
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE /2) + adjx, top + int(TILESIZE /2) +adjy
    DISPLAYSURF.blit(textSurf, textRect) 
    
def makeText(text,color,bgcolor,top,left):
    #Create the Surface and rect objects for some text/
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return(textSurf, textRect)
    
def drawBoard(board, message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf,textRect = makeText(message,MESSAGECOLOR,BGCOLOR,5,5)
        DISPLAYSURF.blit(textSurf,textRect)
    
    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex,tiley,board[tilex][tiley])
                
    left, top = getLeftTopOfTile(0,0)
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF,BOARDCOLOR, (left -5, top -5,width +11, height +11), 4)
    DISPLAYSURF.blit(RESET_SURF,RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)

def slideAnimation(board, direction, message, animationSpeed):
    #Note: This function does not check if the move is valid.
    
    blankx,blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky 
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky 
    
    # prepare the base surface
    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy()
    # draw a blank space over the moving tile on the baseSurf Surface/
    moveLeft, moveTop = getLeftTopOfTile(movex,movey)
    pygame.draw.rect(baseSurf,BGCOLOR,(moveLeft, moveTop, TILESIZE, TILESIZE))
    for i in range(0,TILESIZE, animationSpeed):
        #animate the tile sliding over
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0,0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateNewPuzzle(numSlides):
    #Form a starting configuration, make numSlides number of move and animate these moves).
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) # pauses 5000 milliseconds for effect
    lastMove =None
    for i in range(numSlides):
        move = getRandomMove(board,lastMove)
        slideAnimation(board, move, 'Generating new puzzle...', int(TILESIZE /3))
        makeMove(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)
    
def resetAnimation(board, allMoves):
    # make all of the moves in allMoves in reverse.
    revAllMove = allMoves[:] # get a copy of the list
    revAllMove.reverse()
    
    for move in revAllMove:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == LEFT:
            oppositeMove = RIGHT
        elif move == RIGHT:
            oppositeMove = LEFT
        slideAnimation(board, oppositeMove, '',int(TILESIZE /2))
        makeMove(board, oppositeMove)
        
if __name__ =='__main__':
    main()
