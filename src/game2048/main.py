from .output import *
from .gameCore import *
import os
from subprocess import run


if os.name == "nt":
    import msvcrt
    clearTerminalCommand = "cls"

    def readKey():
        key = msvcrt.getwch()
        if key == "\x03":
            raise KeyboardInterrupt()
        return key

else:
    from getkey import getkey
    clearTerminalCommand = "clear"

    def readKey():
        return getkey()


def continueGame(printGameBoardFunc, gameList):
    run(clearTerminalCommand, shell=True)
    newPointCords = generateNewCords(gameList)
    gameList[newPointCords[0]][newPointCords[1]] = chooseNewNum(getScore())
    printGameBoardFunc(gameList, getScore())


def main():
    run(clearTerminalCommand, shell=True)
    printStartScreen()

    while True:
        try:
            pressedKey = readKey()
        except KeyboardInterrupt:
            return
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
                run(clearTerminalCommand, shell=True)
                howToPlay()
            elif pressedKey == "b" or pressedKey == "B":
                run(clearTerminalCommand, shell=True)
                printStartScreen()
            elif pressedKey == "q" or pressedKey == "Q":
                return

    gameList = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    continueGame(updateGameBoardFunc, gameList)

    while True:
        try:
            pressedKey = readKey()
        except KeyboardInterrupt:
            break
        else:
            if pressedKey == "w" or pressedKey == "W":
                prevGameList = gameList
                updatedVerticalList = handleVerticalLines(gameList, "up")
                gameList = convertVerticalLines(updatedVerticalList)
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc, gameList)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break

            elif pressedKey == "s" or pressedKey == "S":
                prevGameList = gameList
                updatedVerticalList = handleVerticalLines(gameList, "down")
                gameList = convertVerticalLines(updatedVerticalList)
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc, gameList)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break

            elif pressedKey == "d" or pressedKey == "D":
                prevGameList = gameList
                gameList = handleHorizontalLines(gameList, "right")
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc, gameList)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break

            elif pressedKey == "a" or pressedKey == "A":
                prevGameList = gameList
                gameList = handleHorizontalLines(gameList, "left")
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc, gameList)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break

            elif pressedKey == "q" or pressedKey == "Q":
                break


if __name__ == "__main__":
    main()
