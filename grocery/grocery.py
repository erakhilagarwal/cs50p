def main():
    ask_for_grocery()

def ask_for_grocery():
    grocery = {}
    while(True):
        try:
            item = input()
            item = item.strip().upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            for item in sorted(grocery.keys()):
                print(f"{grocery[item]} {item}")
            break
        except KeyError:
            grocery[item] = 1

main()