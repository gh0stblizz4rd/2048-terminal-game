from output import *
from gameCore import *
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
        key = getkey()
        return key

run(clearTerminalCommand, shell=True)
printStartScreen()


        
if __name__ == "__main__":

    while True:
        try:
            pressedKey = readKey()
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
                run(clearTerminalCommand, shell=True)
                howToPlay()
            elif pressedKey == "b" or pressedKey == "B":
                run(clearTerminalCommand, shell=True)
                printStartScreen()
            elif pressedKey == "q" or pressedKey == "Q":
                exit(0)


    def continueGame(printGameBoardFunc):
        run(clearTerminalCommand, shell=True)
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
            pressedKey = readKey()
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
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break

            elif pressedKey == "s" or pressedKey == "S":
                prevGameList = gameList
                updatedVerticalList = handleVerticalLines(gameList, "down")
                gameList = convertVerticalLines(updatedVerticalList)
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break
            
            elif pressedKey == "d" or pressedKey == "D":
                prevGameList = gameList
                gameList = handleHorizontalLines(gameList, "right")
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break

            elif pressedKey == "a" or pressedKey == "A":
                prevGameList = gameList
                gameList = handleHorizontalLines(gameList, "left")
                if gameStatus(prevGameList, gameList):
                    continueGame(updateGameBoardFunc)
                else:
                    run(clearTerminalCommand, shell=True)
                    gameOver(getScore(), colored)
                    break
            elif pressedKey == "q" or pressedKey == "Q":
                break
