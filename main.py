from output import *
from gameCore import *
from getkey import getkey
from subprocess import run

run(["clear"])
printStartScreen()


while True:
    try:
        pressedKey = getkey()
    except KeyboardInterrupt:
        exit(0)
    else:
        if pressedKey == "s" or pressedKey == "S":
            updateGameBoardFunc = coloredGameBoard
            colored = True
            break
        elif pressedKey == "u" or pressedKey == "U":
            updateGameBoardFunc = legacyGameBoard
            colored = False
            break
        elif pressedKey == "h" or pressedKey == "H":
            run(["clear"])
            howToPlay()
        elif pressedKey == "b" or pressedKey == "B":
            run(["clear"])
            printStartScreen()
        elif pressedKey == "q" or pressedKey == "Q":
            exit(0)


def continueGame(printGameBoardFunc):
    run(["clear"])
    newPointCords = generateNewCords(gameList)
    gameList[newPointCords[0]][newPointCords[1]] = chooseNewNum(getScore())
    printGameBoardFunc(gameList, getScore())


gameList = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


continueGame(updateGameBoardFunc)



while True:

    try:
        pressedKey = getkey()
    except KeyboardInterrupt:
        break
    else:
        if pressedKey == "w" or pressedKey == "W":
            prevGameList = gameList
            updatedVerticalList = handleVerticalLines(gameList, "up")
            gameList = convertVerticalLines(updatedVerticalList)
            if gameStatus(prevGameList, gameList):
                continueGame(updateGameBoardFunc)
            else:
                run(["clear"])
                gameOver(getScore(), colored)
                break

        elif pressedKey == "s" or pressedKey == "S":
            prevGameList = gameList
            updatedVerticalList = handleVerticalLines(gameList, "down")
            gameList = convertVerticalLines(updatedVerticalList)
            if gameStatus(prevGameList, gameList):
                continueGame(updateGameBoardFunc)
            else:
                run(["clear"])
                gameOver(getScore(), colored)
                break
        
        elif pressedKey == "d" or pressedKey == "D":
            prevGameList = gameList
            gameList = handleHorizontalLines(gameList, "right")
            if gameStatus(prevGameList, gameList):
                continueGame(updateGameBoardFunc)
            else:
                run(["clear"])
                gameOver(getScore(), colored)
                break

        elif pressedKey == "a" or pressedKey == "A":
            prevGameList = gameList
            gameList = handleHorizontalLines(gameList, "left")
            if gameStatus(prevGameList, gameList):
                continueGame(updateGameBoardFunc)
            else:
                run(["clear"])
                gameOver(getScore(), colored)
                break
