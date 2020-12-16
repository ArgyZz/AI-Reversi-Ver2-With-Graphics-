import pygame

def m_input(screen):
    loop = True
    clock = pygame.time.Clock()
    while (loop):
        screen.fill((0, 92, 9))
        textFont = pygame.font.Font(pygame.font.get_default_font(), 40)
        textSurface = textFont.render('Select Tile', False, (0, 0, 0))
        optionFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        tipFont = pygame.font.Font(pygame.font.get_default_font(), 20)
        option1 = optionFont.render('Black', False, (0, 0, 0))
        option2 = optionFont.render('White', False, (0, 0, 0))
        tip = tipFont.render('Tip: Blacks play first', False, (0, 0, 0))
        screen.blit(textSurface, (320, 80))
        screen.blit(option1, (365, 240))
        screen.blit(option2, (365, 320))
        screen.blit(tip, (550, 700))
        mouse = pygame.mouse.get_pos()

        if 425 > mouse[0] > 365 and 265 > mouse[1] > 240:
            option1 = optionFont.render('Black', False, 'white')
            screen.blit(option1, (368, 240))
        if 422 > mouse[0] > 363 and 342 > mouse[1] > 319:
            option2 = optionFont.render('White', False, 'white')
            screen.blit(option2, (368, 320))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 425 > mouse[0] > 365 and 265 > mouse[1] > 240:
                    loop = False
                    return ['X', 'O']
                elif 422 > mouse[0] > 363 and 342 > mouse[1] > 319:
                    loop = False
                    return ['O', 'X']
            pygame.display.update()
            clock.tick(15)

def playInput(screen, moveArray, tile):
    if(tile=='X'):
        str = 'Make a move (Black)'
    else:
        str = 'Make a move (White)'
    while True:
        textFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        select = textFont.render(str, False, (0, 0, 0))
        screen.blit(select, (20, 50))
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(8):
                    for j in range(8):
                        if int(moveArray[i][j][0][0]) <= mouse[1] <= int(moveArray[i][j][0][1]):
                            if int(moveArray[i][j][1][0]) <= mouse[0] <= int(moveArray[i][j][1][1]):

                                return (i+1, j+1)





def moves():
    x = 126
    y = 126
    step = 60
    innerstep = 10
    vmoves = []
    for i in range(8):
        vmoves.append(['']*8)
    for i in range(8):
        x = 126
        y += innerstep
        for j in range(8):
            x += innerstep
            vmoves[i][j] = ((x, x+step), (y, y+step))
            x += step
        y += step
    return vmoves

def marble(screen, marble, xpos, ypos):
    pygame.draw.circle(screen, marble, (xpos, ypos), 15)

def drawGrid(screen):
    for x in range(8):
        for y in range(8):
            rect = pygame.Rect(x*70+120, y*70+120, 70, 70)              
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

def menu(screen):
    loop = True
    play = False
    clock = pygame.time.Clock()

    while(loop):
        screen.fill((0, 92, 9))
        textFont = pygame.font.Font(pygame.font.get_default_font(),40)
        textSurface = textFont.render('Welcome to Reversi', False, (0,0,0))
        optionFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        option1 = optionFont.render('Play', False, (0, 0, 0))
        option2 = optionFont.render('Quit', False, (0, 0, 0))
        screen.blit(textSurface, (230,80))
        screen.blit(option1, (365, 320))
        screen.blit(option2, (365, 380))
        mouse = pygame.mouse.get_pos()
        if 425 > mouse[0] > 365 and 345 > mouse[1] > 320:
            option1 = optionFont.render('Play', False, 'white')
            screen.blit(option1, (368, 320))
        if 422 > mouse[0] > 363 and 402> mouse[1] > 379:
            option2 = optionFont.render('Quit', False, 'white')
            screen.blit(option2, (368, 380))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 425 > mouse[0] > 365 and 345 > mouse[1] > 320:
                    loop = False
                    play = True
                elif 422 > mouse[0] > 363 and 402 > mouse[1] > 379:
                    loop = False
                    play = False
                    pygame.quit()
            pygame.display.update()
            clock.tick(15)
    return play

def gamemode(screen):
    clock = pygame.time.Clock()
    loop = True
    while (loop):
        screen.fill((0, 92, 9))
        textFont = pygame.font.Font(pygame.font.get_default_font(), 40)
        optionFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        textSurface = textFont.render('Select Mode', False, (0, 0, 0))
        option1 = optionFont.render('Player VS PC', False, (0, 0, 0))
        option2 = optionFont.render('PC VS PC', False, (0, 0, 0))
        option3 = optionFont.render('Player VS Player', False, (0, 0, 0))
        screen.blit(option1, (320, 270))
        screen.blit(option2, (345, 340))
        screen.blit(option3, (300, 410))
        screen.blit(textSurface, (300, 80))
        mouse = pygame.mouse.get_pos()
        if 480 > mouse[0] > 320 and 295 > mouse[1] > 267:
            option1 = optionFont.render('Player VS PC', False, 'white')
            screen.blit(option1, (323, 270))
        if 462 > mouse[0] > 342 and 365 > mouse[1] > 337:
            option2 = optionFont.render('PC VS PC', False, 'white')
            screen.blit(option2, (348, 340))
        if 505 > mouse[0] > 300 and 435 > mouse[1] > 410:
            option3 = optionFont.render('Player VS Player', False, 'white')
            screen.blit(option3, (303, 410))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 > mouse[0] > 320 and 295 > mouse[1] > 267:
                    loop = False
                    return '1'
                elif 462 > mouse[0] > 342 and 365 > mouse[1] > 337:
                    loop = False
                    return '2'
                elif 505 > mouse[0] > 300 and 435 > mouse[1] > 410:
                    loop = False
                    return '3'
            pygame.display.update()
            clock.tick(15)

def difficulty(screen):
    clock = pygame.time.Clock()
    loop = True
    while (loop):
        screen.fill((0, 92, 9))
        textFont = pygame.font.Font(pygame.font.get_default_font(), 40)
        optionFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        textSurface = textFont.render('Select Difficulty', False, (0, 0, 0))
        screen.blit(textSurface, (265, 80))
        option1 = optionFont.render('Easy', False, (0, 0, 0))
        option2 = optionFont.render('Medium', False, (0, 0, 0))
        option3 = optionFont.render('Hard', False, (0, 0, 0))
        screen.blit(option1, (370, 235))
        screen.blit(option2, (355, 295))
        screen.blit(option3, (370, 355))
        mouse = pygame.mouse.get_pos()
        if 430 > mouse[0] > 370 and 258 > mouse[1] > 235:
            option1 = optionFont.render('Easy', False, 'white')
            screen.blit(option1, (373, 235))
        if 445 > mouse[0] > 355 and 315 > mouse[1] > 290:
            option2 = optionFont.render('Medium', False, 'white')
            screen.blit(option2, (358, 295))
        if 435 > mouse[0] > 365 and 375 > mouse[1] > 353:
            option3 = optionFont.render('Hard', False, 'white')
            screen.blit(option3, (373, 355))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 430 > mouse[0] > 370 and 258 > mouse[1] > 235:
                    pygame.display.update()
                    loop = False
                    return 3
                elif 445 > mouse[0] > 355 and 315 > mouse[1] > 290:
                    loop = False
                    return 4
                elif 435 > mouse[0] > 365 and 375 > mouse[1] > 353:
                    loop = False
                    return 9
            pygame.display.update()
            clock.tick(15)

def drawBoard_graphics(board, screen, b_marble, w_marble, positions, score, msg='', pos=0):
    clock = pygame.time.Clock()
    screen.fill((0, 92, 9))
    textFont = pygame.font.Font(pygame.font.get_default_font(), 30)
    gprint(score, screen)
    if(len(msg)>0):
        m1 = textFont.render(msg, False, (0, 0, 0))
        if(pos==1):
            screen.blit(m1, (480, 50))
        elif(pos==2):
            screen.blit(m1, (400, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    drawGrid(screen)
    pygame.display.update()

    for i in range(8):
        for j in range(8):
            if (board[i][j] == 'X'):
                marble(screen, b_marble, positions[i][0][0], positions[0][j][1])
                pygame.display.update()
            elif (board[i][j] == 'O'):
                marble(screen, w_marble, positions[i][0][0], positions[0][j][1])
                pygame.display.update()

def playAgain(screen, msg1, msg2):
    # Returns true if the player wants to play again. False otherwise.
    loop = True
    play = False
    clock = pygame.time.Clock()

    while (loop):
        screen.fill((0, 92, 9))
        textFont = pygame.font.Font(pygame.font.get_default_font(), 40)
        textSurface = textFont.render('Play Again?', False, (0, 0, 0))
        optionFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        score = optionFont.render(msg1, False, (0, 0, 0))
        winner = optionFont.render(msg2, False, (0, 0, 0))
        option1 = optionFont.render('Yes', False, (0, 0, 0))
        option2 = optionFont.render('No', False, (0, 0, 0))
        screen.blit(textSurface, (280, 270))
        screen.blit(score, (50, 80))
        screen.blit(winner, (50, 160))
        screen.blit(option1, (355, 380))
        screen.blit(option2, (360, 440))
        mouse = pygame.mouse.get_pos()
        if 400 > mouse[0] > 352 and 402 > mouse[1] > 378:
            option1 = optionFont.render('Yes', False, 'white')
            screen.blit(option1, (358, 380))
        if 397 > mouse[0] > 357 and 461 > mouse[1] > 436:
            option2 = optionFont.render('No', False, 'white')
            screen.blit(option2, (363, 440))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 > mouse[0] > 352 and 402 > mouse[1] > 378:
                    loop = False
                    play = True
                elif 397 > mouse[0] > 357 and 461 > mouse[1] > 436:
                    loop = False
                    play = False
                    pygame.quit()
            pygame.display.update()
            clock.tick(15)
    return play

def gprint(str, screen):
    textFont = pygame.font.Font(pygame.font.get_default_font(), 20)
    score = textFont.render('SCORE', False, (0, 0, 0))
    nscore = textFont.render(str, False, (0, 0, 0))
    screen.blit(score, (360, 700))
    screen.blit(nscore, (220, 750))