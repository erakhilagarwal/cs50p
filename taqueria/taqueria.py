def main():
    get_order()

def get_order():
    total = 0;
    while True:
        try:
            item = input("Enter item: ")
            item = item.strip().title()
            total += menu[item]
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break;
        except KeyError:
            pass

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()