import random
import sys
from pyfiglet import Figlet

def main():
    if(len(sys.argv) != 1 and len(sys.argv) != 3):
        sys.exit("Invalid usage")

    figlet = Figlet()
    figletFonts = figlet.getFonts()

    if(len(figletFonts) == 0):
        sys.exit("Figlet fonts not found")

    if(len(sys.argv) == 3):
        if(sys.argv[1] != "-f" and sys.argv[1] != "--font"):
            sys.exit("Invalid usage")
        if(sys.argv[2] not in figletFonts):
            sys.exit("Invalid usage")
        ufont = sys.argv[2]
    else:
        ufont = random.choice(figletFonts)

    figlet.setFont(font=ufont)
    inputStr = input()
    print(figlet.renderText(inputStr))

if(__name__ == "__main__"):
    main()