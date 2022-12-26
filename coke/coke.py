def main():
    amount = 50
    userAmount = 0
    amountDue = amount - userAmount
    while(True):
        print(f"Amount Due: {amountDue}")
        insertedCoin = getUserInput()
        if acceptsCoin(insertedCoin):
            userAmount += int(insertedCoin)
            amountDue = amount - userAmount
        if(userAmount >= amount):
            break
    print(f"Change Owed: {userAmount - amount}")

def acceptsCoin(coin):
    match coin:
        case "25" | "10" | "5":
            return True
    return False;

def getUserInput():
    return input("Insert Coin: ").strip()

if __name__ == "__main__":
    main()