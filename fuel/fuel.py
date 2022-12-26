def main():
    res = get_guage()
    if res <= 1:
        print("E")
    elif res >= 99:
        print("F")
    else:
        print(f"{res}%")

def get_guage() :
    while True:
        try:
            inputStr = input("Guage: ")
            num, ope, den = inputStr.partition("/")
            num = int(num)
            den = int(den)
            if num > den:
                continue
            res = int(round((num * 100) / den, 0));
            return res
        except (ValueError, ZeroDivisionError):
            pass

main()
