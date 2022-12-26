def main():
    inptStr = getUserInput()
    for c in inptStr:
        print("", end="") if isVowel(c) else print(c, end="")
    print()

def isVowel(char):
    match char.lower():
        case "a" | "e" | "i" | "o" | "u":
            return True
    return False;

def getUserInput():
    return input("Input String: ")

if __name__ == "__main__":
    main()