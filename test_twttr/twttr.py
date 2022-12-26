def main():
    inptStr = getUserInput()
    print(shorten(inptStr))

def shorten(word = ""):
    ret = ""
    for c in word:
        #if not(isVowel(c)):
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            ret += c
    return ret

def isVowel(char):
    match char.lower():
        case "a" | "e" | "i" | "o" | "u":
            return True
    return False;

def getUserInput():
    return input("Input String: ")

if __name__ == "__main__":
    main()