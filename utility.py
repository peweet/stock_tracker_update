from datetime import datetime, timedelta

def calculate_percentage_change(day1 : float, day2 : float):
    if day1 == day2:
        return 100.0
    try:
        return round((abs(day1 - day2) / day2) * 100.0, 2)
    except ZeroDivisionError:
        return 0
def return_date(delta: int):
    yesterday = datetime.now() - timedelta(delta)
    yesterday= datetime.strftime(yesterday, '%Y-%m-%d')
    return yesterday
