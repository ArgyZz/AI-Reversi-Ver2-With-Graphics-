# Koutsompinas Giorgos 3150251
# Velaoras Apostolos 3180249
# Kaldis Argyrios 3160045

import sys
import time
import math
import random

import pip._internal as pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    m = ''
    while(m!='Y' and m!='N'):
        print('Do you want to play with graphics? (You can also play with cmd)')
        m = input('Type your answer [Y/N]: ').upper()
    if(m == 'Y'):
        try:
            import pygame
            cmd = False
            import graphics
        except ImportError:
            answer = ''
            while(answer!="Y" and answer !="N"):
                print("Could not detect 'pygame' graphics package...\nDo you want to install it?\n(type NO to play with cmd...)\n")
                answer = input("Type your answer [Y/N]: ").upper()
                if(answer == "Y"):
                    try:
                        install('pygame')
                        import pygame
                        cmd = False
                        import graphics
                    except:
                        cmd = True
                        print('Unknown error occurred...\ncmd mode on...\n')
                else: cmd = True
    else:
        print('cmd mode on...')
        cmd = True




def AlphaBeta(board, tile, depth, alpha, beta, maxPlayer):

    boardCp= getBoardCp(board)
    if depth == 0 or getValidMoves(board,tile)==[]:
        score = getScore(boardCp)[playerTile]
        return score

    if maxPlayer:
        maxEval = -math.inf
        for x in range(8):
            for y in range(8):
                if isValidMove(board,tile ,x, y):
                    makeMove(boardCp, tile, x ,y)
                    eval = AlphaBeta(boardCp, tile, depth - 1, alpha, beta, False)
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break # beta cut-off
        return maxEval
    else: #minPlayer
        minEval = math.inf
        for x in range(8):
            for y in range(8):
                if isValidMove(board, tile, x , y):
                    makeMove(boardCp,tile ,x ,y)
                    eval = AlphaBeta(boardCp, playerTile, depth - 1, alpha, beta, True)
                    #print('This is the player tile '+ playerTile)
                    minEval = min(minEval,eval)
                    beta=min(beta,eval)
                    if beta <= alpha:
                        break # alpha cut-off

        return minEval

def giveDepth():
    depthIn = '1 2 3 4 5 6 7 8 9 10'.split()
    while True:
        answer=input("Give the depth of the search(10 is Max):  ")
        if answer in depthIn:
            answer = int(answer)
            break
        else:
            print("Wrong input.Please try again(Number between 1-10)")
    return answer

def drawBoard(board):# Draws the board.
    LINE = ' +---+---+---+---+---+---+---+---+'
    COLUMN = ' |   |   |   |   |   |   |   |   |'
    print('   1   2   3   4   5   6   7   8')
    print(LINE)
    for y in range(8):
        print(COLUMN)
        print(y+1, end="")
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(COLUMN)
        print(LINE)


def boardReset(board): # Resets the board to its starting point.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
# Starting pieces.
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():# Creates an empty new board.
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board

def isOnBoard(x, y):# Returns True if the coordinates located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7

def isValidMove(board, tile, xvector, yvector): # Returns False if the player's move in invalid.
 # If the move is valid,it returns a list of all the possible moves the player can make

    if board[xvector][yvector] != ' ' or not isOnBoard(xvector, yvector): # Checks if x nad y vector are between 1-8 and if tile is empty.
        return False            # Returns false if not empty or no on board.
    board[xvector][yvector] = tile # Temporarily set the tile on the board.
    if tile == 'X':
        oppTile = 'O'
    else:
        oppTile = 'X'
    tilesToFlip = []
    for xmove, ymove in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        #Checks if the player has valid moves in every possible cordination from the move that the player has selected.
        x, y = xvector, yvector
        x += xmove
        y += ymove
        if isOnBoard(x, y) and board[x][y] == oppTile: # If it is on board and if tile in this direction is the opponents tile then.....
                                                       # There is a piece belonging to the computer
            x += xmove
            y += ymove
            if not isOnBoard(x, y):
                continue
            while board[x][y] == oppTile: # Repeat the process.
                x += xmove
                y += ymove
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True: # Appends the list with every cordinational compination that has the opponents tile on it.
                    x -= xmove
                    y -= ymove
                    if x == xvector and y == yvector:
                        break           # Break if reach the original space.
                    tilesToFlip.append([x, y])
    board[xvector][yvector] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip      # Return list.

def getBoardCp(board): # Make a duplicate of the board list and return the duplicate.
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard


def getValidMoves(board, tile):
    # Returns a list of [x,y] valid moves for the given player on the given board.
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScore(board):
    # Return the score for each player by counting the tiles in the board.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    # Lets the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Please select tile between X and O.(Tip: If you want to play first type X.): ')
        tile = input().upper()
    # the first element in the list is the player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def playAgain():
    # Returns true if the player wants to play again. False otherwise.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, tile, xvector, yvector):
    # Place the tile on the board at xvector, yvector, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xvector, yvector)
    if tilesToFlip == False:
        return False
    board[xvector][yvector] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getPlayerMove(board, playerTile): # Lets the player type in their move.
    # Returns the move as [x, y] or returns the string quit.
    checkMove = '1 2 3 4 5 6 7 8'.split()
    while True:
        if(cmd == True):
            print('Enter your move, or type quit to end the game.')
            move = input().lower()
        else:
            smove = graphics.playInput(screen, moveArray, playerTile)
            move = str(smove[0]) + str(smove[1])

        if move == 'quit':
            return 'quit'
        if len(move) == 2 and move[0] in checkMove and move[1] in checkMove:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            if(cmd==True):
                print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
                print('For example, 81 will be the top-right corner.')
    return [x, y]

def getComputerMove(board,tile,depth,minEval, maxEval,):
    maxPoints = -1
    bestX = -1;
    bestY = -1
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile ,x,y):
                #makeMove(getBoardCp(board), tile,x,y)
                points = AlphaBeta(board, tile, depth, minEval, maxEval, True)
                if points >= maxPoints:
                        maxPoints = points
                        bestX = x; bestY = y
    return (bestX, bestY)



def graphicsScore(playerTile, computerTile):
    # Prints out the current score.
    scores = getScore(mainBoard)

    scoremsg = black +'(black): ' + str(scores['X']) + ' - ' + white +'(white): ' + str(scores['O'])
   
    if(cmd==True):
        print(scoremsg)
    return scoremsg



def selectMode():
    mode = ''

    while not(mode == '1' or mode == '2' or mode == '3'):
        print('Please select the mode you want this program to proceed.(Tip: 1: Pc vs Player, 2: Pc vs Pc, 3: Player vs PLayer)')
        mode = input()
    return mode



def randomTiles():
    tiles=['X','x','o','O']
    choosenTile=random.choice(tiles).upper()
    return choosenTile



def selectDifficulty():
    levels = '1 2 3'.split()

    while True:
        diff = input('Select difficulty level.(Tip: 1: Easy , 2: Medium , 3: Hard).')
        if diff in levels:
            break
        else:
            print("Wrong input.Please try again(Number between 1-10)")
    depth=randomDepth(int(diff))
    return depth


def randomDepth(level):
    if(level=='1'):
        depth=random.randint(1,3)
    elif(level=='2'):
        depth = random.randint(4, 6)
    else:
        depth = random.randint(7, 10)
    return depth

def randomDeapth():
    depth=random.randint(1,10)
    depth = random.randint(1,depth)
    return depth




# The game is begining !!!!!!!
# The game is begining !!!!!!!
# The game is begining !!!!!!!
# The game is begining !!!!!!!
# The game is begining !!!!!!!
if (cmd == False):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill((0, 92, 9))

    pygame.display.set_caption("Reversi")
    b_marble = (20, 20, 20)
    w_marble = (235, 235, 235)

        # top left = 155, 155, step = 70


    xx = 85 #add/remove 70 for next block
    yy = 85 
    positions = []
    for i in range(8):
        positions.append([0]*8)

    for i in range(8):
        xx += 70
        for j in range(8):
            yy += 70
            positions[i][j] = (xx, yy)

# The game is begining !!!!!!!
# The game is begining !!!!!!!
# The game is begining !!!!!!!
# The game is begining !!!!!!!

if(cmd==True): print('Welcome to Reversi!')

while True:

    if(cmd == False):
        moveArray = graphics.moves()
        play = graphics.menu(screen)
        if play == False:
            quit()
        mode = graphics.gamemode(screen)
        if(mode != '3'):
            depth = graphics.difficulty(screen)
        else:
            depth = randomDeapth()
    else:
        mode = selectMode()
        if (mode == '1'):
            depth = selectDifficulty()
        else:
            depth = randomDeapth()
    # Reset the board and game.
    mainBoard = getNewBoard()
    boardReset(mainBoard)

    if(mode=='1' or mode == '3'):
        if(cmd == True):
            playerTile, computerTile = enterPlayerTile()
        else: playerTile, computerTile = graphics.m_input(screen)
        if  playerTile== 'X':
            if(mode=='3'):
                black = 'Player1'
                white = 'Player2'
            else:
                black = 'Player'
                white = 'Computer'
            turn = 'player'
        else:
            if(mode=='3'):
                black = 'Player2'
                white = 'Player1'
            else:
                black = 'Computer'
                white = 'Player'
                turn='computer'
        msg1 = 'The ' + turn + ' will go first.'
        score = graphicsScore(playerTile, computerTile)
        if(cmd==True):
            print(msg1)
        else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score, msg1, 1)
        while True:
            if turn == 'player':
                # Player's turn.
                score = graphicsScore(playerTile, computerTile)
                if(cmd == True): drawBoard(mainBoard)
                else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score)

                move = getPlayerMove(mainBoard, playerTile)
                if move == 'quit':
                    if(cmd==True):
                        print('Thanks for playing!')
                    sys.exit() # terminate the program
                else:
                    makeMove(mainBoard, playerTile, move[0], move[1])
                if getValidMoves(mainBoard, computerTile) == []:
                    break
                else:
                    turn = 'computer'
            else:
                if(mode=='1'):
                    score = graphicsScore(playerTile, computerTile)
                    if(cmd == True): drawBoard(mainBoard)
                    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score)

                    msg2 = "Computer's turn.Waiting..."
                    if(cmd==True): print(msg2)
                    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score, msg2, 2)

                    #Wait for computer move
                    now = time.time()
                    after= now + 1
                    while time.time() < after:
                        pass
                    x,y =getComputerMove(mainBoard,computerTile,depth,-math.inf,math.inf)
                    makeMove(mainBoard, computerTile, x, y)
                    if getValidMoves(mainBoard, playerTile) == []:
                        break
                    else:

                        turn = 'player'
                else:
                    # Player's 2 turn.
                    score = graphicsScore(playerTile, computerTile)
                    if(cmd == True): drawBoard(mainBoard)
                    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score)


                    move = getPlayerMove(mainBoard, computerTile)
                    if move == 'quit':
                        if (cmd == True):
                            print('Thanks for playing!')
                        sys.exit()  # terminate the program
                    else:
                        makeMove(mainBoard, computerTile, move[0], move[1])
                    if getValidMoves(mainBoard, playerTile) == []:
                        break
                    else:
                        turn = 'player'


    elif(mode == '2'):
        choosenTile= randomTiles()
        if  choosenTile == 'X':
            turn ='1stPc'
            black = 'Computer 1'
            white = 'Computer 2'
            playerTile = 'O'
            if(cmd == True):
                print('Pc 1 has X')
                print('Pc 2 has O')
        else:
            turn='2ndPc'
            playerTile = 'X'
            black = 'Computer 2'
            white = 'Computer 1'
            if(cmd == True):
                print('Pc 1 has O')
                print('Pc 2 has X')
        msg1 = 'The ' + turn + ' will go first.'
        if(cmd==True): print(msg1)
        while True:
            # Pc1 turn.
                if turn=='1stPc':
                    score = graphicsScore(choosenTile, playerTile)
                    if(cmd == True): drawBoard(mainBoard)
                    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score)


                    msg2 = turn +' turn.Waiting....'
                    if(cmd==True): print(msg2)
                    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score , msg2, 1)

                    # Wait for computer move
                    now = time.time()
                    after = now + 1
                    while time.time() < after:
                        pass
                    x, y = getComputerMove(mainBoard, choosenTile, depth, -math.inf, math.inf)
                    makeMove(mainBoard, choosenTile, x, y)
                    if getValidMoves(mainBoard, playerTile) == []:
                        break
                    else:

                        turn = '2ndPc'
                else:
                    score = graphicsScore(choosenTile, playerTile)
                    if(cmd == True): drawBoard(mainBoard)
                    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score)


                    msg2 = turn + ' turn. Waiting...'
                    if (cmd == True):
                        print(msg2)
                    else:
                        graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score, msg2, 1)
                    # Wait for computer move
                    now = time.time()
                    after = now + 1
                    while time.time() < after:
                        pass
                    x, y = getComputerMove(mainBoard, playerTile, depth, -math.inf, math.inf)
                    makeMove(mainBoard, playerTile, x, y)
                    if getValidMoves(mainBoard, choosenTile) == []:
                        break
                    else:

                        turn = '1stPc'


    # Display the final score.
    if(mode=='2'):
        computerTile=choosenTile
    if (cmd == True): drawBoard(mainBoard)
    else: graphics.drawBoard_graphics(mainBoard, screen, b_marble, w_marble, positions, score)
    scores = getScore(mainBoard)
    if(cmd==True):
        print('X scored %s points. O scored %s points.' % (scores['O'],scores['X']))
        if scores[playerTile] > scores[computerTile]:
            if(mode!='2' and mode!='3'):
                print('You beat the computer by %s points! Congratulations!' %(scores[playerTile] - scores[computerTile]))
        elif scores[playerTile] < scores[computerTile]:
            if(mode!='2' and mode!='3'):
                print('You lost. The computer beat you by %s points.' %(scores[computerTile] - scores[playerTile]))
        else:
            print('The game was a tie!')

        if not playAgain():
            break
    else:
        bscore = scores['X']
        wscore = scores['O']
        endmsg = 'Black: ' + str(bscore) + ' - ' + 'White: ' + str(wscore)
        if(bscore>wscore):
            endmsg2 = black+' won!'
        elif(bscore<wscore):
            endmsg2 = white + ' won!'
        else:
            endmsg2 = 'Tie!'
        graphics.playAgain(screen, endmsg, endmsg2)
