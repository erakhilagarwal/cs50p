import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip = ip.strip()
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255 and re.match(r"^(0|([^0]\d{0,2}))$", n), m.groups()))

if __name__ == "__main__":
    main()