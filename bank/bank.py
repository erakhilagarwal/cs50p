def main():
    greet = input("Hey : ")
    pay = validateGreeting(greet)
    print(f"${pay}")

def validateGreeting(s):
    s = s.strip().lower()
    if(s.startswith("hello")):
        return 0;
    elif(s.startswith("h")):
        return 20;
    else:
        return 100;


main()