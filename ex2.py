import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = [] # Empty list initialization

    # Checking that input values are correct. Returning empty list in case of they are not
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return lottery_numbers

    # Filling the list with random values
    while len(lottery_numbers) < quantity:
        value = random.randint(min, max)
        if value in lottery_numbers: # Checking if currently generated value is already in list
            continue
        lottery_numbers.append(value)
    lottery_numbers.sort() # List sorting
    return lottery_numbers # List returning
    # The task is done, function returns sorted list with randomly generated values


# Debuging module
print("\n")
print(get_numbers_ticket(10, 9, 5))