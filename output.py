from colored import Fore, Back, Style


gridColor = f"{Back.rgb(120, 120, 120)}"
textColor = f"{Fore.rgb(0, 0, 0)}"
whiteBg = f"{Back.white}{Fore.black}"
whiteFg = f"{Fore.white}"

asciiLogo = """  
  /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
 /$$__  $$ /$$$_  $$| $$  | $$ /$$__  $$
|__/  \ $$| $$$$\ $$| $$  | $$| $$  \ $$
  /$$$$$$/| $$ $$ $$| $$$$$$$$|  $$$$$$/
 /$$____/ | $$\ $$$$|_____  $$ >$$__  $$
| $$      | $$ \ $$$      | $$| $$  \ $$
| $$$$$$$$|  $$$$$$/      | $$|  $$$$$$/
|________/ \______/       |__/ \______/ 
"""

gameInstructions = """
2048 is a captivating puzzle game where the objective is to combine 
numbered tiles to increment numbers on the tiles. With each move, 
a new tile - either a "2" or a "4" - appears in a random empty spot 
on the board. Tiles with the same number merge when they collide, 
creating a new tile with a value that is the sum of the two merged 
tiles. The game ends when the board fills up and there are no more 
moves available. To succeed, plan your moves carefully, aiming to 
consolidate higher-numbered tiles in one corner while keeping your 
options open for future merges. Enjoy!
"""


def centerText(text, lenght, colored=True):
    remaningSpaces = lenght - len(text)

    if remaningSpaces <= 0:
        return f"{textColor if colored else ''}{text[:lenght]}{Style.reset if colored else ''}"

    devision = int(remaningSpaces / 2)
    if remaningSpaces % 2 != 0:
        reminder = remaningSpaces % 2

        return f"{' '*int(devision+reminder)}{textColor if colored else ''}{text}{' '*devision}{Style.reset if colored else ''}"
    
    return f"{' '*devision}{textColor if colored else ''}{text}{' '*devision}{Style.reset if colored else ''}"


def howToPlay():
    print("\n")

    for line in gameInstructions.splitlines():
        print(" "*10+line)
    
    print("\n"*2)
    print(centerText("Use WASD keys to move the game tiles", 84, colored=False))
    print(centerText("Press B to return", 84, colored=False))
    print("\n"*2)




def printStartScreen():
    print("\n"*3)
    for line in asciiLogo.splitlines():
        print(" "*15, end='')
        for char in line:
            if char == "$":
                print(f"{whiteBg}{char}{Style.reset}", end='')
            else:
                print(char, end='')

        print("")
    print("\n"*3)

    print(centerText(f"{whiteBg}Choose an option by pressing a key{Style.reset}\n", 93))
    print(f"{' '*26}{whiteFg}S - Start game{Style.reset}")
    print(f"{' '*26}{whiteFg}U - Uncolored mode{Style.reset}")
    print(f"{' '*26}{whiteFg}H - How to play{Style.reset}")
    print(f"{' '*26}{whiteFg}Q - Quit{Style.reset}")
    print("\n"*3)    
   

def getNumberColor(number):
    if number == 0:
        return f"{Back.rgb(232, 232, 232)}"
    elif number == 2:
        return f"{Back.rgb(234, 208, 150)}"
    elif number == 4:
        return f"{Back.rgb(205, 173, 102)}"
    elif number == 8:
        return f"{Back.rgb(233, 173, 38)}"
    elif number == 16:
        return f"{Back.rgb(201, 119, 12)}"
    elif number == 32:
        return f"{Back.rgb(207, 90, 10)}"
    elif number == 64:
        return f"{Back.rgb(182, 79, 10)}"
    elif number == 128:
        return f"{Back.rgb(231, 216, 13)}"
    elif number == 256:
        return f"{Back.rgb(202, 189, 19)}"
    elif number == 512:
        return f"{Back.rgb(179, 160, 13)}"
    elif number == 1024:
        return f"{Back.rgb(126, 112, 10)}"
    elif number == 1024:
        return f"{Back.rgb(126, 112, 10)}"
    elif number == 2048:
        return f"{Back.rgb(240, 120, 5)}"
    elif number == 4096:
        return f"{Back.rgb(233, 97, 10)}"
    elif number == 8192:
        return f"{Back.rgb(209, 84, 4)}"
    elif number == 8192:
        return f"{Back.rgb(218, 81, 17)}"
    elif number == 8192:
        return f"{Back.rgb(218, 81, 17)}"
    elif number == 16384:
        return f"{Back.rgb(193, 42, 2)}"
    elif number > 16384:
        return f"{Back.rgb(2, 56, 194)}"


def coloredGameBoard(numbersList, score):
    print("\n"*3)
    print(f"{' '*65}")

    for line in numbersList:
        lineIndex = numbersList.index(line)

        color0 = getNumberColor(line[0])
        color1 = getNumberColor(line[1])
        color2 = getNumberColor(line[2])
        color3 = getNumberColor(line[3])

        print(f"         ", end="")
        print(f"{color0}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color1}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color2}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color3}{' '*13}{Style.reset}")
        print("         ", end="")
        print(f"{color0}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color1}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color2}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color3}{' '*13}{Style.reset}")

        print("         ", end="")
        print(f"{color0}{centerText(str(numbersList[lineIndex][0]), 13)}{gridColor} {Style.reset}", end="")
        print(f"{color1}{centerText(str(numbersList[lineIndex][1]), 13)}{gridColor} {Style.reset}", end="")
        print(f"{color2}{centerText(str(numbersList[lineIndex][2]), 13)}{gridColor} {Style.reset}", end="")
        print(f"{color3}{centerText(str(numbersList[lineIndex][3]), 13)}{Style.reset}")

        print("         ", end="")
        print(f"{color0}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color1}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color2}{' '*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color3}{' '*13}{Style.reset}")
        print("         ", end="")

        lowerChar = "_"
        if lineIndex == 3:
            lowerChar = " "

        print(f"{color0}{lowerChar*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color1}{lowerChar*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color2}{lowerChar*13}{Style.reset}{gridColor} {Style.reset}", end="")
        print(f"{color3}{lowerChar*13}{Style.reset}")

    print("\n")
    print(f"{' '*53}{whiteBg}{textColor}Score: {score}{Style.reset}")
    print("\n"*2)


def legacyGameBoard(numbersList, score):
    print("\n"*3)
    print(f"          .......................................................")
    print(f"         |             |             |             |             |")
    print(f"         |             |             |             |             |")
    print(f"         |{centerText(str(numbersList[0][0]), 13, colored=False)}|{centerText(str(numbersList[0][1]), 13, colored=False)}|{centerText(str(numbersList[0][2]), 13, colored=False)}|{centerText(str(numbersList[0][3]), 13, colored=False)}|")
    print(f"         |             |             |             |             |")
    print(f"         |_____________|_____________|_____________|_____________|")
    print(f"         |             |             |             |             |")
    print(f"         |             |             |             |             |")
    print(f"         |{centerText(str(numbersList[1][0]), 13, colored=False)}|{centerText(str(numbersList[1][1]), 13, colored=False)}|{centerText(str(numbersList[1][2]), 13, colored=False)}|{centerText(str(numbersList[1][3]), 13, colored=False)}|")
    print(f"         |             |             |             |             |")
    print(f"         |_____________|_____________|_____________|_____________|")
    print(f"         |             |             |             |             |")
    print(f"         |             |             |             |             |")
    print(f"         |{centerText(str(numbersList[2][0]), 13, colored=False)}|{centerText(str(numbersList[2][1]), 13, colored=False)}|{centerText(str(numbersList[2][2]), 13, colored=False)}|{centerText(str(numbersList[2][3]), 13, colored=False)}|")
    print(f"         |             |             |             |             |")
    print(f"         |_____________|_____________|_____________|_____________|")
    print(f"         |             |             |             |             |")
    print(f"         |             |             |             |             |")
    print(f"         |{centerText(str(numbersList[3][0]), 13, colored=False)}|{centerText(str(numbersList[3][1]), 13, colored=False)}|{centerText(str(numbersList[3][2]), 13, colored=False)}|{centerText(str(numbersList[3][3]), 13, colored=False)}|")
    print(f"         |             |             |             |             |")
    print(f"         |             |             |             |             |")
    print(f"         ```````````````````````````````````````````````````````")
    print("")
    print(f"{' '*53}Score: {score}")
    print("\n"*2)


def gameOver(score, colored):
    if colored:
        scoreNumLine = f"{whiteBg}##{Style.reset}{centerText(f'{whiteFg}Score: {score}{Style.reset}', 32, colored=False)}{whiteBg}##{Style.reset}"

        print("\n"*7, end='')
        print(centerText(f"{whiteBg}{'#'*22}{Style.reset}", 90))
        print(centerText(f"{whiteBg}##{Style.reset}{' '*18}{whiteBg}##{Style.reset}", 113))
        print(centerText(f"{whiteBg}##{Style.reset}    {whiteFg}Game over!{Style.reset}    {whiteBg}##{Style.reset}", 128, colored=False))
        print(centerText(scoreNumLine, 127, colored=False))
        print(centerText(f"{whiteBg}##{Style.reset}{' '*18}{whiteBg}##{Style.reset}", 113))
        print(centerText(f"{whiteBg}{'#'*22}{Style.reset}", 90))
        print("\n"*7, end='')
    
    else:
        scoreNumLine = f"##{centerText(f'Score: {score}', 18, colored=False)}##"

        print("\n"*7, end='')
        print(centerText(f"{'#'*22}", 68, colored=False))
        print(centerText(f"##{' '*18}##", 68, colored=False))
        print(centerText(f"##    Game over!    ##", 68, colored=False))
        print(centerText(scoreNumLine, 68, colored=False))
        print(centerText(f"##{' '*18}##", 68, colored=False))
        print(centerText(f"{'#'*22}", 68, colored=False))
        print("\n"*7, end='')

