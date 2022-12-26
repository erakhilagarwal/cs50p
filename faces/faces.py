
#main function
def main():
    inputStr = input("Enter your message: ")
    result = convert(inputStr)
    print(f"{result}")

#conver function uses replace to replace ":)" with "🙂" and ":(" "🙁"
def convert(rawStr):
    rawStr = rawStr.replace(":)", "🙂")
    rawStr = rawStr.replace(":(", "🙁")
    return rawStr

#calling main function
main()