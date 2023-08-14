from datetime import datetime
from sys import argv


def is_valid_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# user_date = "32.05.2020"

def check_date(str_date: str):
    if is_valid_date(str_date):
        if is_leap_year(int(str_date.split(".")[-1])):
            print("The date is valid and year is leap")
        else:
            print("The date is valid,but year isn't leap")
    else:
        print("The date isn't valid")


print("start")
check_date(argv[1])
print("stop")
# please use "python check_correct_date.py 30.05.2020"  in terminal
