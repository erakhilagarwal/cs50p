def main():
    convert_outdated()

def convert_outdated():
    while True:
        try:
            inputDate = input("Date: ")
            inputDate = inputDate.strip()
            date, month, year = get_day_month_year(inputDate)
            print(f"{year:04}-{month:02}-{date:02}")
            return
        except EOFError:
            return
        except (ValueError, KeyError, Exception):
            pass

def get_day_month_year(inpDate):
    if inpDate.find("/") != -1:
        month, date, year = inpDate.split("/")
    elif inpDate.find(","):
        date_month, year = inpDate.rsplit(",")
        month, date = date_month.split()
        month = month.title()
        month = months.index(month) + 1
    month = int(month)
    date = int(date)
    year = int(year)
    if(year <= 0):
        raise Exception("YearError")
    if(month <=0 or month > 12):
        raise Exception("MonthError")
    if(date <= 0 or date > days_in_month(month, year)):
        raise Exception("DateError")
    return [date, month, year]

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def days_in_month(month, year):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 29 if year % 4 == 0 else 28
    return 0;

main()
