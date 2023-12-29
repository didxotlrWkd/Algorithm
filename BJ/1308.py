import sys

input = sys.stdin.readline

today_year, today_month, today_day = map(int, input().split())
Dday_year, Dday_month, Dday_day = map(int, input().split())

day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_cal(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    total_days = 0

    for y in range(1, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_in_month[m]

    total_days += day

    return total_days

today_count = day_cal(today_year, today_month, today_day)
Dday_count = day_cal(Dday_year, Dday_month, Dday_day)

if Dday_year - today_year > 1000 or \
    (Dday_year - today_year == 1000 and Dday_month > today_month) or \
    (Dday_year - today_year == 1000 and Dday_month == today_month and Dday_day >= today_day):
    print('gg')
else:
    print(f"D-{Dday_count - today_count}")
