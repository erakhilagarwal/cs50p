def main():
    ans = input("answer to the Great Question of Life, the Universe and Everything? ")
    if matchAnswer(ans):
        print("Yes")
    else:
        print("No")

def matchAnswer(s):
    fs = s.strip().lower()
    match fs:
        case "42" | "forty-two" | "forty two" :
            return True
        case _:
            return False
    return False

main()