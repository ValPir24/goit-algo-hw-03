from datetime import datetime

def get_upcoming_birthdays(users):
    today = datetime.today().date() # Obtaining current date
    birthdays = [] # Initializing of empty list of congratulatins
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #  Current user birthday date obtaining
        birthday_this_year = datetime(today.year, today.month, birthday_date.day).date() # Date of birthday THIS year
        if birthday_this_year < today: # Checking if birthday was before today
            continue
        elif (birthday_this_year - today).days < 7: # Checking if birthday will be in nearest 7 days
            if datetime.weekday(birthday_this_year) == 5: # Checking if birthday in on Saturday
                birthday_this_year = datetime(birthday_this_year.year, birthday_this_year.month, birthday_this_year.day + 2).date() # Changing the day to Monday
                user.pop("birthday")
                user["congratulation_date"] = datetime.strftime(birthday_this_year,"%Y.%m.%d") # Adding the date to dictionary
                birthdays.append(user) # Adding dictionary to list
            elif datetime.weekday(birthday_this_year) == 6: # Checking if birthday in on Sunday
                birthday_this_year = datetime(birthday_this_year.year, birthday_this_year.month, birthday_this_year.day + 1).date() # Changing the day to Monday
                user.pop("birthday")
                user["congratulation_date"] = datetime.strftime(birthday_this_year,"%Y.%m.%d") # Adding the date to dictionary
                birthdays.append(user) # Adding dictionary to list
            else:
                user.pop("birthday")
                user["congratulation_date"] = datetime.strftime(birthday_this_year,"%Y.%m.%d") # Adding the date to dictionary
                birthdays.append(user) # Adding dictionary to list
    return birthdays # Returning the list
    # The task is done, function returns list of dictionaris with names and dates of congratulations

# Debuging module
users = [
    {"name": "John Doe", "birthday": "1985.01.31"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
    {"name": "Benny Benassi", "birthday": "1990.01.28"},
    {"name": "Keyley Smith", "birthday": "1980.01.01"},
    {"name": "John Kelly", "birthday": "1996.01.30"}
]
print(get_upcoming_birthdays(users))