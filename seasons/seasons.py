from datetime import date
import sys
import inflect

class MyDate:
    @classmethod
    def diff_from_today(cls, input):
        today = date.today()
        try:
            indate = date.fromisoformat(input)
        except (ValueError, TypeError):
            sys.exit("Invalid date")
        else:
            diff = today - indate
            diff_min = diff.days * 24 * 60
            return diff_min

    @classmethod
    def in_str(cls, minutes):
        p = inflect.engine()
        min_str = p.number_to_words(minutes, andword="")
        return f"{min_str.capitalize()} minutes"

def main():
    birthday = input("Date of Birth: ")
    diff_min = MyDate.diff_from_today(birthday)
    print(f"{MyDate.in_str(diff_min)}")

def get_valid_date(s):
    try:
        d = date.fromisoformat(s)
        return d
    except (TypeError, ValueError):
        sys.exit("Invalid date")

def get_today_difference(d):
    try:
        today = date.today()
        diff = today - d
        return diff.days
    except ValueError:
        sys.exit("Invalid date")

def get_string_minutes(num_days):
    p = inflect.engine()
    min = num_days * 24 * 60
    min_str = p.number_to_words(min, andword="")
    return f"{min_str.capitalize()} minutes"

if __name__ == "__main__":
    main()