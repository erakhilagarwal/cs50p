def main():
    timeStr = input("What's time now? ")
    time = convert(timeStr)
    if 7 <= time <= 8:
        print("breakfast time ")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    time = time.strip()
    hours, minutes = time.split(":")
    rtime = float(hours) + round((float(minutes) / 60), 2)
    return rtime

if __name__ == "__main__":
    main()