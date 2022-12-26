import random

def main():
    level = get_number("Level: ")
    num = random.randint(1, level)
    guess = 0
    while(guess != num):
        guess = get_number("Guess: ")
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break;


def get_number(prompt):
    while(True):
        try:
            num = input(prompt)
            num = int(num.strip())
            if(num > 0) :
                return num
        except ValueError:
            pass


if(__name__ == "__main__"):
    main()