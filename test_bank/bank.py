def main():
    greet = input("Hey : ")
    pay = value(greet)
    print(f"${pay}")

def value(greeting = ""):
    s = greeting.strip().lower()
    if(s.startswith("hello")):
        return 0;
    elif(s.startswith("h")):
        return 20;
    else:
        return 100;

if __name__ == "__main__":
    main()