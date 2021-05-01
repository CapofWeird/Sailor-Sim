"""This file handles date and time manipulation"""


def check_leap_year(year: int) -> bool:
    """Checks whether the given year is a leap year"""
    if ((year % 4) == 0):
        is_leap_year = True
        if ((year % 100) == 0):
            is_leap_year = False
            if ((year % 400) == 0):
                is_leap_year = True
    else:
        is_leap_year = False

    return is_leap_year


def update_time(current_time: list, update_minute=0, update_hour=0,
                update_day=0, update_month=0, update_year=0) -> list:
    """Updates the program clock to represent the passage of time.
       I sure hope I can figure out some other way to do this because
       gosh dangit it's ugly
       """
    months_31_days = [1, 3, 5, 7, 8, 10, 12]  # Months with 31 days in them
    current_time[0] += update_minute
    current_time[1] += update_hour
    current_time[2] += update_day
    current_time[3] += update_month
    current_time[4] += update_year
    # Are the minutes equal to or over 60?
    if (current_time[0] >= 60):
        current_time[0] -= 60
        current_time[1] += 1
    # Are the hours over 24?
    if (current_time[1] > 24):
        current_time[1] -= 24
        current_time[2] += 1
    # Is it a new month?
    # 31 day months
    if (current_time[3] in months_31_days):
        if (current_time[2] > 31):
            current_time[2] -= 31
            current_time[3] += 1
    # 30 day monthes
    elif (current_time[3] != 2):
        if (current_time[2] > 30):
            current_time[2] -= 30
            current_time[3] += 1
    # February
    else:
        # Leap year February
        if (check_leap_year(current_time[4])):
            if (current_time[2] > 29):
                current_time[2] -= 29
                current_time[3] += 1
        # Normal year February
        else:
            if (current_time[2] > 28):
                current_time[2] -= 28
                current_time[3] += 1
    # Is it a new year?
    if (current_time[3] > 12):
        current_time[3] -= 12
        current_time[4] += 1

    return current_time
