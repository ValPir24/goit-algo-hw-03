import re

def normalize_phone(phone_number):
    pattern = r"[\d\+]+" # Pattern creation. Meaning one or more occurrences of digits or plus signs
    phone_number=''.join(re.findall(pattern,phone_number)) # Joining all found occurrences in one string
    if phone_number[0] == "0":
        phone_number = "+38" + phone_number # If number starts with zero then add "+380" country code
    elif phone_number[0] == "3":
        phone_number = "+" + phone_number # If number starts with number three then add plus sign
    return phone_number # Returning phone number
    # The task is done, function returns number in propper format

# Debuging module
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)   
