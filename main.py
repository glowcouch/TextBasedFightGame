import os

worldWidth = 20
worldHeight = 20

print(type(worldHeight))

playerX = 0
playerY = 0

def renderScreen():
    os.system("clear")
    for y in range(0 - (int(20 / 2)), int(20 / 2)):
        for x in range(0 - (20 / 2), 20 / 2):
            if x == playerX and y == playerY:
                print(":)", end="")
            else:
                print("00", end="")
        print("")


while True:
    inp = input()

    if inp == "w":
        playerY -= 1
    if inp == "s":
        playerY += 1
    if inp == "a":
        playerX -= 1
    if inp == "d":
        playerX += 1

    if playerX > 10:
        playerX = 10
    if playerX < -10:
        playerX = -10
    if playerY < -10:
        playerY = -10
    if playerY > 10:
        playerY = 10
    renderScreen()