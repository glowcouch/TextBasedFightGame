import os
import csv

map = []
collectedCoins = []

def loadRoom(roomNumber):
    map.clear()
    with open("Room"+str(roomNumber)+".csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            map.append(row)
    for y in range(0, worldHeight):
        for x in range(0, worldWidth):
            if map[y][x] == "c":
                for coin in collectedCoins:
                    if x == coin[0] and y == coin[1]:
                        map[y][x]=" "

worldWidth = 20
worldHeight = 20

print(type(worldHeight))

playerX = 10
playerY = 15
money = 0

loadRoom(1)

def renderScreen():
    os.system("clear")
    print("money: "+str(money))
    for y in range(0, worldHeight):
        for x in range(0, worldWidth):
            if x == playerX and y == playerY:
                print("🙂", end="")
            elif map[y][x] == "w":
                print("██", end="")
            elif map[y][x] == "c":
                print("◉ ", end="")
            elif map[y][x] == " ":
                print("  ", end="")
            else:
                print(" |", end="")
        print("")

renderScreen()
print("Type WASD and press enter to move.")
while True:
    inp = input()

    if inp == "w" and map[playerY-1][playerX] != "w":
        playerY -= 1
    if inp == "s" and map[playerY+1][playerX] != "w":
        playerY += 1
    if inp == "a" and map[playerY][playerX-1] != "w":
        playerX -= 1
    if inp == "d" and map[playerY][playerX+1] != "w":
        playerX += 1

    if map[playerY][playerX] == "c":
        money+=1
        map[playerY][playerX] = " "
        collectedCoins.append([playerX, playerY])
    elif "d" in map[playerY][playerX]:
        _, room, entryX, entryY = map[playerY][playerX].split(":")
        loadRoom(room)
        playerX = int(entryX)
        playerY = int(entryY)

    if playerX > worldWidth:
        playerX = worldWidth
    if playerX < 0:
        playerX = 0
    if playerY < 0:
        playerY = 0
    if playerY > worldHeight:
        playerY = worldHeight
    renderScreen()