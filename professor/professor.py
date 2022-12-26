import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        if question_answer(level):
            score += 1
    print(f"Score: {score}")

def get_level():
    while(True):
        try:
            level = input("Level: ")
            level = int(level.strip())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level in [1, 2, 3]:
        min, max = get_level_min_max(level)
        return random.randint(min, max)
    raise ValueError

def get_level_min_max(level):
    match level:
        case 1:
            return [0, 9]
        case 2:
            return [10, 99]
        case 3:
            return [100, 999]
    raise ValueError

def question_answer(level):
    x = generate_integer(level)
    y = generate_integer(level)
    sol = x + y
    for _ in range(3):
        try:
            userSol = int(input(f"{x} + {y} = ").strip())
            if sol == userSol:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
            pass
    print(f"{x} + {y} = {sol}")
    return False

if __name__ == "__main__":
    main()