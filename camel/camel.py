def main():
    camel = getUserInput()
    for s in camel:
        print(f"_{s.lower()}", end="") if s.isupper() else print(f"{s}", end="")
    print()


def getUserInput():
    return input("CamelCase: ")

if __name__ == "__main__":
    main()