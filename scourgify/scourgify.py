import sys
import csv
from pathlib import Path

def main():
    before, after = get_commandline_arguments(2, 2)
    try:
        students = []
        is_valid_file_type(before)
        is_valid_file_type(after)
        with open(before, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["last"], _,row["first"] = [i.strip() for i in row["name"].partition(",")]
                students.append(row)
    except (FileNotFoundError, PermissionError):
        sys.exit(f"Could not read {before}")
    try:
        with open(after, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"], extrasaction="ignore")
            writer.writeheader()
            for row in students:
                writer.writerow(row)
    except (FileNotFoundError, PermissionError):
        sys.exit(f"Could not write {after}")

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
    if file.rfind(".") == -1:
        sys.exit(f"Not a {file_type} file")
    if not(file.endswith(file_ext)):
        sys.exit(f"Not a {file_type} file")
    return True

if __name__ == "__main__":
    main()