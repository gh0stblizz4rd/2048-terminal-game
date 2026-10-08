
# A command line terminal version of the 2048 game

  

Implementation of the famous [2048 game](https://play2048.co/) that can be played directly from the command line.

  

<p>

<img  src="https://i.imgur.com/gryAQou.png"  width="400px"/>

<img  src="https://i.imgur.com/52DRou7.png"  width="400px"/>

</p>

  

### Installation (Using pipx)
**For windows:**

python3 -m pip install pipx

pipx ensurepath

pipx install git+https://github.com/gh0stblizz4rd/2048-terminal-game.git
   
 game2048
 
**Linux (debian based distros):**

sudo apt update

sudo apt install pipx

pipx ensurepath

pipx install git+https://github.com/gh0stblizz4rd/2048-terminal-game.git

game2048
  

## Controls

  

- WASD for moving the game board

- Q to quit the game

  

### Dependencies

  

- [colored](https://pypi.org/project/colored/) - Used for displaying colorful text in the terminal.

- [getkey](https://pypi.org/project/getkey/) - Used for detecting user keyboard input. (Unix based systems only)