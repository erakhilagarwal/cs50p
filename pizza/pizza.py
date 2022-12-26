import sys
import csv
from pathlib import Path
from tabulate import tabulate

def main():
    file_name, *_ = get_commandline_arguments()
    try:
        pizza = []
        is_valid_file_type(file_name)
        with open(file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                pizza.append(row)
            print(tabulate(pizza, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def get_commandline_arguments(min = 1, max = 1):
    if len(sys.argv) < min + 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > max + 1:
        sys.exit("Too many command-line arguments")
    return sys.argv[1:]

def is_valid_file_type(file = "", file_ext = ".csv", file_type = "CSV"):
    file = file.strip()
    if file == "":
        sys.exit("No file name specified")
    path = Path(file)
    if not(path.is_file()):
        sys.exit("File does not exist")
    if file.rfind(".") == -1:
        sys.exit(f"Not a {file_type} file")
    if not(file.endswith(file_ext)):
        sys.exit(f"Not a {file_type} file")
    return True

if __name__ == "__main__":
    main()