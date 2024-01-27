import datetime

def get_days_from_today(date):

    # Error handling module
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except (ValueError, TypeError):
        print("Oops...invalid input")
        exit()

    # Days difference caclulation
    date_today = datetime.datetime.today()
    delta = date_today - date
    return delta.days
    # The task is done, function returns days difference


# Debuging module
print("\n")
print(f"The difference between dates in days: {get_days_from_today("2014-05-02")}")

