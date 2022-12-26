def main():
    res = get_guage()
    print(gauge(res))

def get_guage() :
    while True:
        try:
            inputStr = input("Guage: ")
            return convert(inputStr)
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    num, _, den = fraction.partition("/")
    num = int(num)
    den = int(den)
    if num > den and den > 0:
        raise ValueError("X greator than Y")
    res = int(round((num * 100) / den, 0));
    print(f"here {res}")
    return res


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()