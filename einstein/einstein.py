def main():
    userInput = input("Enter mass: ")
    mass = int(userInput)
    energy = getEnergy(mass)
    print(f"{energy}")

def getEnergy(mass):
    c = 300000000
    energy = mass * pow(c, 2)
    return energy

main()