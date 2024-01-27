import re

dirty=["    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
]

def norm_phone(phone_number):
    p1 = r"[\d\+]+"
    phone_number_step1 = "".join(re.findall(p1,phone_number))
    for number in pho


for phone in dirty:
    print(norm_phone(phone))