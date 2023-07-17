import sys
import random
import pygame

birth = ""
pygame.init()
board = [["0", "0", "0", "0", ], ["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]]
board1 = [["0", "0", "0", "0", ], ["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]]
length1 = [["35", "35", "35", "35", ], ["35", "35", "35", "35"], ["35", "35", "35", "35"], ["35", "35", "35", "35"]]
generate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
list1 = [2, 2, 4]
screen = pygame.display.set_mode((800, 600))
grey = (100, 100, 100)
white = (255, 255, 255)
pygame.display.set_caption("2048")
xPos = 180
yPos = 90
font = pygame.font.Font('FreeSansBold.ttf', 45)
text = font.render(birth, True, white)
textrect = text.get_rect()


def disp():
    print("-----------------")
    for v in range(0, 4):
        print(board[v])
    print("-----------------")


def gen():
    for geep in range(0, 4):
        for glen in range(0, 4):
            if board[geep][glen] == "0":
                board[geep][glen] = str(random.choice(generate))


def redraw():
    xPos1 = 180
    yPos1 = 90
    for this in range(0, 4):
        for that in range(0, 4):
            if board[this][that] == "0":
                board1[this][that] = ""
            else:
                board1[this][that] = board[this][that]
            if len(str(board[this][that])) == 1:
                length1[this][that] = 35
            elif len(str(board[this][that])) == 2:
                length1[this][that] = 25
            elif len(str(board[this][that])) == 3:
                length1[this][that] = 12
            elif len(str(board[this][that])) == 4:
                length1[this][that] = 0
            pygame.draw.rect(screen, grey, pygame.Rect(xPos1, yPos1, 100, 100))
            glumbo = font.render(board1[this][that], True, white)
            textrect.center = (xPos1 + int(length1[this][that]), yPos1 + 50)
            screen.blit(glumbo, textrect)
            pygame.display.flip()
            xPos1 += 110
        yPos1 += 110
        xPos1 = 180


def wincheck():
    for test in range(0, 4):
        for test1 in range(0, 4):
            if board[test][test1] == "2048":
                print("you win")
                pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 10000, 10000))
                win = font.render("You Win!", True, white)
                textrect.center = (300, 300)
                screen.blit(win, text--rect)


for i in range(0, 4):
    for y in range(0, 4):
        pygame.draw.rect(screen, grey, pygame.Rect(xPos, yPos, 100, 100))
        textrect.center = (xPos + 50, yPos + 50)
        screen.blit(text, textrect)
        pygame.display.flip()
        xPos += 110
    yPos += 110
    xPos = 180
counter = 0
StartingPos = 0
while StartingPos != 2:
    xPos = 180
    yPos = 90
    x = random.randint(0, 16)
    counter = 0
    for m in range(0, 4):
        for n in range(0, 4):
            counter += 1
            if counter == x and board[m][n] == "0":
                birth = str(random.choice(list1))
                board[m][n] = birth
                StartingPos = StartingPos + 1
                text = font.render(birth, True, white)
                textrect.center = (xPos + int(length1[m][n]), yPos + 50)
                screen.blit(text, textrect)
                pygame.display.flip()
            elif counter == x and board[m][n] != "0":
                x = random.randint(0, 16)
            xPos += 110
        yPos += 110
        xPos = 180
disp()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
                move_done = 0
                for h in range(3, 0, -1):
                    for r in range(0, 4):
                        if board[h][r] == "0" or h - 1 <= -1:
                            continue
                        if board[h - 1][r] == "0":
                            board[h - 1][r] = board[h][r]
                            board[h][r] = "0"
                        if board[h - 1][r] == board[h][r]:
                            board[h - 1][r] = str(int(board[h][r]) * 2)
                            board[h][r] = "0"
                        move_done = 1
                if move_done == 1:
                    gen()
                disp()
                redraw()
                wincheck()
            if event.key == pygame.K_DOWN:
                print("down")
                move_done = 0
                for h in range(0, 4):
                    for r in range(0, 4):
                        if board[h][r] == "0" or h + 1 > 3:
                            continue
                        if board[h + 1][r] == "0":
                            board[h + 1][r] = board[h][r]
                            board[h][r] = "0"
                        if board[h + 1][r] == board[h][r]:
                            board[h + 1][r] = str(int(board[h][r]) * 2)
                            board[h][r] = "0"
                        move_done = 1
                if move_done == 1:
                    gen()
                disp()
                redraw()
                wincheck()
            if event.key == pygame.K_LEFT:
                print("left")
                move_done = 0
                for h in range(0, 4):
                    for r in range(3, 0, -1):
                        if board[h][r] == "0" or r - 1 <= -1:
                            continue
                        if board[h][r - 1] == "0":
                            board[h][r - 1] = board[h][r]
                            board[h][r] = "0"
                        if board[h][r - 1] == board[h][r]:
                            board[h][r - 1] = str(int(board[h][r]) * 2)
                            board[h][r] = "0"
                        move_done = 1
                if move_done == 1:
                    gen()
                disp()
                redraw()
                wincheck()
            if event.key == pygame.K_RIGHT:
                move_done = 0
                for h in range(0, 4):
                    for r in range(0, 4):
                        if board[h][r] == "0" or r + 1 > 3:
                            continue
                        if board[h][r + 1] == "0":
                            board[h][r + 1] = board[h][r]
                            board[h][r] = "0"
                        if board[h][r + 1] == board[h][r]:
                            board[h][r + 1] = str(int(board[h][r]) * 2)
                            board[h][r] = "0"
                        move_done = 1
                if move_done == 1:
                    gen()
                disp()
                redraw()
                wincheck()
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
