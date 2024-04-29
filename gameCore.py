from random import randint

gameScore = 0


def generateNewCords(gamelist):
    while True:
        cords = randint(0, 3), randint(0, 3)
        if gamelist[cords[0]][cords[1]] == 0:
            break
    return cords


def chooseNewNum(score):
    if score <= 150:
        return 2

    numList = [2, 4]
    index = randint(0, 1)
    return numList[index]


def splitVerticalLines(gamelist):
    verticalLines = []
    lineIndex = -1

    for lineIndex in range(0, 4):
        line = []

        for numberIndex in range(0, 4):
            line.append(
                gamelist[numberIndex][lineIndex]
            )
        verticalLines.append(line)
    
    return verticalLines


def convertVerticalLines(lineslist):
    gameList = [[], [], [], []]

    for index in range(0, 4):
        for verticalLine in lineslist:
            gameList[index].append(verticalLine[index])
    
    return gameList


def lineDownward(line):
    global gameScore

    numberIndex = -1
    lostLines = 0
    for number in line:
        numberIndex += 1
        if number != 0:
            remainingList = line[numberIndex+1:4]
            remainingNumbers =  list(filter(lambda num: num != 0, remainingList))


            if remainingNumbers == []:
                return [0, 0, 0, number]


            elif line == [number] * 4:
                gameScore += number*4
                return [0, 0, number*2, number*2]


            elif len(remainingNumbers) == 2:

                if (remainingNumbers[0] == number and
                remainingNumbers[1] == number):
                    gameScore += number*2
                    return [0, 0, number, number*2]


                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number):
                    gameScore += number*2
                    return [0, 0, number*2, remainingNumbers[1]]

                elif (remainingNumbers[0] == remainingNumbers[1] and
                remainingNumbers[0] != number):
                    gameScore += remainingNumbers[0]*2
                    return [0, 0, number, remainingNumbers[0]*2] 


            elif len(remainingNumbers) == 3:

                if (remainingNumbers[0] != number and
                    remainingNumbers[1] == remainingNumbers[2]):
                    gameScore += remainingNumbers[1]*2
                    return [0, number, remainingNumbers[0], remainingNumbers[1]*2]

                elif (remainingNumbers[0] != number and
                    remainingNumbers[0] == remainingNumbers[1]):
                    gameScore += remainingNumbers[0]*2
                    return [0, number, remainingNumbers[0]*2, remainingNumbers[2]]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [0, number*2, remainingNumbers[1], remainingNumbers[2]]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] == number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [0, number, number*2, remainingNumbers[2]]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] == number):
                    gameScore += remainingNumbers[1]*2
                    return [0, number*2, remainingNumbers[1], number]


            elif len(remainingNumbers) == 1:
                if number in remainingNumbers:
                    gameScore += number*2
                    return [0, 0, 0, number*2]
            
            numZeros = 3 - len(remainingNumbers)
            return [0]*numZeros + [number] + remainingNumbers


    return [0, 0, 0, 0]


def lineUpward(line):
    global gameScore

    numberIndex = -1
    for number in line:
        numberIndex += 1
        if number != 0:
            remainingList = line[numberIndex+1:4]
            remainingNumbers =  list(filter(lambda num: num != 0, remainingList))


            if remainingNumbers == []:
                return [number, 0, 0, 0]


            elif line == [number] * 4:
                gameScore += number*4
                return [number*2, number*2, 0, 0]


            elif len(remainingNumbers) == 2:

                if (remainingNumbers[0] == number and
                remainingNumbers[1] == number):
                    gameScore += number*2
                    return [number*2, number, 0, 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number):
                    gameScore += number*2
                    return [number*2, remainingNumbers[1], 0, 0]

                elif (remainingNumbers[0] == remainingNumbers[1] and
                remainingNumbers[0] != number):
                    gameScore += remainingNumbers[0]*2
                    return [number, remainingNumbers[0]*2, 0, 0] 


            elif len(remainingNumbers) == 3:

                if (remainingNumbers[0] != number and
                    remainingNumbers[1] == remainingNumbers[2]):
                    gameScore += remainingNumbers[1]*2
                    return [0, remainingNumbers[0], remainingNumbers[1]*2, number]

                elif (remainingNumbers[0] != number and
                    remainingNumbers[0] == remainingNumbers[1]):
                    gameScore += remainingNumbers[0]*2
                    return [number, remainingNumbers[0]*2, remainingNumbers[2], 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [number*2, remainingNumbers[1], remainingNumbers[2], 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] == number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [number, number*2, remainingNumbers[2], 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] == number):
                    gameScore += number*2
                    return [0, number*2, remainingNumbers[1], number]
                
            
            elif len(remainingNumbers) == 1:
                if number in remainingNumbers:
                    gameScore += number*2
                    return [number*2, 0, 0, 0,]

            numZeros = 3 - len(remainingNumbers)
            return [number] + remainingNumbers + [0]*numZeros
    
    return [0, 0, 0, 0]


def lineRight(line):
    global gameScore

    numberIndex = -1
    for number in line:
        numberIndex += 1
        if number != 0:
            remainingList = line[numberIndex+1:4]
            remainingNumbers =  list(filter(lambda num: num != 0, remainingList))

            if remainingNumbers == []:
                return [0, 0, 0, number]


            elif line == [number] * 4:
                gameScore += number*4
                return [0, 0, number*2, number*2]


            elif len(remainingNumbers) == 2:

                if (remainingNumbers[0] == number and
                remainingNumbers[1] == number):
                    gameScore += number*2
                    return [0, 0, number, number*2]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number):
                    gameScore += number*2
                    return [0, 0, number*2, remainingNumbers[1]]

                elif (remainingNumbers[0] == remainingNumbers[1] and
                remainingNumbers[0] != number):
                    gameScore += remainingNumbers[0]*2
                    return [0, 0, number, remainingNumbers[0]*2] 


            elif len(remainingNumbers) == 3:

                if (remainingNumbers[0] != number and
                    remainingNumbers[1] == remainingNumbers[2]):
                    gameScore += remainingNumbers[1]*2
                    return [0, number, remainingNumbers[0], remainingNumbers[1]*2]

                elif (remainingNumbers[0] != number and
                    remainingNumbers[0] == remainingNumbers[1]):
                    gameScore += remainingNumbers[0]*2
                    return [0, number, remainingNumbers[0]*2, remainingNumbers[2]]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [0, number*2, remainingNumbers[1], remainingNumbers[2]]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] == number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [0, number, number*2, remainingNumbers[2]]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] == number):
                    gameScore += number*2
                    return [0, number*2, remainingNumbers[1], number]


            elif len(remainingNumbers) == 1:
                if number in remainingNumbers:
                    gameScore += number*2
                    return [0, 0, 0, number*2]
            
            numZeros = 3 - len(remainingNumbers)
            return [0]*numZeros + [number] + remainingNumbers

    return [0, 0, 0, 0]


def lineLeft(line):
    global gameScore

    numberIndex = -1
    for number in line:
        numberIndex += 1
        if number != 0:
            remainingList = line[numberIndex+1:4]
            remainingNumbers =  list(filter(lambda num: num != 0, remainingList))


            if remainingNumbers == []:
                return [number, 0, 0, 0]


            elif line == [number] * 4:
                gameScore += number*4
                return [number*2, number*2, 0, 0]


            elif len(remainingNumbers) == 2:

                if (remainingNumbers[0] == number and
                remainingNumbers[1] == number):
                    gameScore += number*2
                    return [number*2, number, 0, 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number):
                    gameScore += number*2
                    return [number*2, remainingNumbers[1], 0, 0]

                elif (remainingNumbers[0] == remainingNumbers[1] and
                remainingNumbers[0] != number):
                    gameScore += remainingNumbers[0]*2
                    return [number, remainingNumbers[0]*2, 0, 0] 


            elif len(remainingNumbers) == 3:

                if (remainingNumbers[0] != number and
                    remainingNumbers[1] == remainingNumbers[2]):
                    gameScore += remainingNumbers[1]*2
                    return [0, remainingNumbers[0], remainingNumbers[1]*2, number]

                elif (remainingNumbers[0] != number and
                    remainingNumbers[0] == remainingNumbers[1]):
                    gameScore += remainingNumbers[0]*2
                    return [number, remainingNumbers[0]*2, remainingNumbers[2], 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [number*2, remainingNumbers[1], remainingNumbers[2], 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] == number and
                remainingNumbers[2] != number):
                    gameScore += number*2
                    return [number, number*2, remainingNumbers[2], 0]

                elif (remainingNumbers[0] == number and
                remainingNumbers[1] != number and
                remainingNumbers[2] == number):
                    gameScore += number*2
                    return [0, number*2, remainingNumbers[1], number]
                
            
            elif len(remainingNumbers) == 1:
                if number in remainingNumbers:
                    gameScore += number*2
                    return [number*2, 0, 0, 0,]

            numZeros = 3 - len(remainingNumbers)
            return [number] + remainingNumbers + [0]*numZeros
    
    return [0, 0, 0, 0]


def handleVerticalLines(gamelist, direction):
    newVerticalLines = []
    verticalLines = splitVerticalLines(gamelist)

    if direction == "down":
        for line in verticalLines:
            newLine = lineDownward(line)
            newVerticalLines.append(newLine)
    
    elif direction == "up":
        for line in verticalLines:
            newLine = lineUpward(line)
            newVerticalLines.append(newLine) 

    return newVerticalLines


def handleHorizontalLines(gamelist, direction):
    newGameList = []

    if direction == "right":
        for line in gamelist:
            newLine = lineRight(line)
            newGameList.append(newLine)
    
    elif direction == "left":
        for line in gamelist:
            newLine = lineLeft(line)
            newGameList.append(newLine) 

    return newGameList


def getScore():
    return gameScore


def gameStatus(prevGameList, currentGameList):
    if (0 not in currentGameList[0] and
        0 not in currentGameList[1] and
        0 not in currentGameList[2] and
        0 not in currentGameList[3] and
        currentGameList == prevGameList):
        return False
    return True