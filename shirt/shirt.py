import sys
import csv
from pathlib import Path
import os

from PIL import Image, ImageOps, UnidentifiedImageError

def main():
    before, after = get_filenames(2, 2)
    check_vald_file_names(before, after)
    if not(os.path.isfile("shirt.png")):
        sys.exit(f"shirt.png does not exist")
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(before) as inp:
                size = shirt.size
                inp = ImageOps.fit(inp, size)
                inp.paste(shirt, shirt)
                inp.save(after)
    except FileNotFoundError:
        sys.exit("Image not found")
    except (UnidentifiedImageError, ValueError, TypeError):
        pass

def get_filenames(min = 1, max = 1):
    if len(sys.argv) < min + 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > max + 1:
        sys.exit("Too many command-line arguments")
    return sys.argv[1:]

def check_vald_file_names(f1 = "", f2 = ""):
    f1 = f1.strip()
    f2 = f2.strip()
    name1, ext1 = os.path.splitext(f1)
    name2, ext2 = os.path.splitext(f2)
    if ext1 not in [".jepg", ".jpg", ".png"]:
        sys.exit(f"Invalid input")
    if ext2 not in [".jepg", ".jpg", ".png"]:
        sys.exit(f"Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    if not(os.path.isfile(f1)):
        sys.exit(f"Input does not exist")
    return True

if __name__ == "__main__":
    main()