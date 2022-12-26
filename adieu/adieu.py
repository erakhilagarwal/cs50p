import inflect

def main():
    p = inflect.engine()
    names = get_names()
    if(len(names) != 0):
        names = p.join(names)
        print(f"Adieu, adieu, to {names}")

def get_names():
    names = []
    while(True):
        try:
            name = input()
            name = name.strip().title()
            names.append(name)
        except EOFError:
            break
    return names


if(__name__ == "__main__"):
    main()