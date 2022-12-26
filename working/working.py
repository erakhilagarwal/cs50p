import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.match(r"(?P<firsthr>\d{1}|1[0-2]{1})(:(?P<firstmin>[0-5][0-9]))? (?P<firsthalf>AM|PM) to (?P<sechr>\d{1}|1[0-2]{1})(:(?P<secmin>[0-5][0-9]))? (?P<sechalf>AM|PM)", s.strip()):
        first = get_time(match.group('firsthr'), match.group('firstmin'), match.group('firsthalf'))
        second = get_time(match.group('sechr'), match.group('secmin'), match.group('sechalf'))
        return f"{first} to {second}"
    else:
        raise ValueError

def get_time(hr, min, midday):
    time = 0
    min_time = 0
    match midday:
        case "AM":
            time += 0
        case "PM":
            time += 12
        case _:
            raise ValueError

    if 1 <= int(hr) <= 11:
        time += int(hr)
    elif int(hr) == 12:
        time += 0
    else:
        raise ValueError
    if min == None:
        min_time += 0
    elif 0 <= int(min) <= 59:
        min_time = int(min)
    else:
        raise ValueError
    return f"{time:02d}:{min_time:02d}"


if __name__ == "__main__":
    main()