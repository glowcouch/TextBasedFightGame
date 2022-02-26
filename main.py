import os

worldWidth = 20
worldHeight = 20

print(type(worldHeight))

playerX = 0
playerY = 0

def renderScreen():
    os.system("clear")
    for y in range(0, worldHeight):
        for x in range(0, worldWidth):
            if x == playerX and y == playerY:
                print(":)", end="")
            else:
                print("00", end="")
        print("")

renderScreen()
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

    if playerX > worldWidth:
        playerX = worldWidth
    if playerX < 0:
        playerX = 0
    if playerY < 0:
        playerY = 0
    if playerY > worldHeight:
        playerY = worldHeight
    renderScreen()