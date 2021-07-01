from datetime import date


def fc_day(month):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return day_dict.get(month)


year, month, day = str(date.today()).split('-')
year, month, day = int(year), int(month), int(day)
day_dict = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

print(fc_day(month))


