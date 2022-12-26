import sys
import os
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]
    print(f"{get_file_code_line_count(file_name)}")

def get_file_code_line_count(file_name = ""):
    if not is_valid_file_type(file_name):
        sys.exit("Unidentified error")
    count = 0
    try:
        with open(file_name, "r") as f :
            for line in f:
                if is_code_line(line):
                    count += 1
        return count
    except PermissionError:
        sys.exit("File is not read allowed")


def is_valid_file_type(file = "", file_ext = ".py"):
    file = file.strip()
    if file == "":
        sys.exit("No file name specified")
    path = Path(file)
    if not(path.is_file()):
        sys.exit("File does not exist")
    if file.rfind(".") == -1:
        sys.exit("Not a Python file")
    if not(file.endswith(file_ext)):
        sys.exit("Not a Python file")
    return True

def is_code_line(line):
    line = line.strip()
    return not(len(line) == 0 or line.isspace() or line.startswith("#"))

if __name__ == "__main__":
    main()
