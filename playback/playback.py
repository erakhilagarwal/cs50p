#take input from user
inputStr = input("Enter What To Say: ")

#parse string into tokens using split and join using "..."
outStr = "...".join(inputStr.split())

print(f"{outStr}")