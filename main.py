import os

worldWidth = 20
worldHeight = 20

print(type(worldHeight))

playerX = 10
playerY = 15
money = 0

map = [
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "w", "w", "w", "w", "w", "w", "w", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "", "", "", "", "", "c", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "w", "w", "w", "", "w", "w", "w", "w", "w", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "w", "", "w", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "w", "", "w", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "w", "w", "w", "w", "", "w", "w", "w", "w", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "c", "", "", "", "", "", "", "", "w", "", "", "", "", ""],
    ["", "", "", "", "", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "", "", "", "", ""]
]

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
            else:
                print("  ", end="")
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
        map[playerY][playerX] = ""

    if playerX > worldWidth:
        playerX = worldWidth
    if playerX < 0:
        playerX = 0
    if playerY < 0:
        playerY = 0
    if playerY > worldHeight:
        playerY = worldHeight
    renderScreen()