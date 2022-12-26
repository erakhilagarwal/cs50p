def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s = ""):
    digitFound = False
    check = is_valid_length(s) and s.isalnum() and s[0:2].isalpha()
    if check:
        for c in s:
            if digitFound:
                check = c.isdigit()
            else:
                check = c != '0';
                digitFound = c.isdigit()
            if(not(check)):
                break
    return check;

def is_valid_length(s = ""):
    return 2 <= len(s) <= 6

if __name__ == "__main__":
    main()