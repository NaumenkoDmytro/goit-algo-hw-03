"""
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку. 
Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. 
Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). 
Це гарантує, що всі номери будуть придатними для відправлення SMS.
"""

import re

def normalize_phone(phone_number: str) ->str:
    pattern = r"\D"
    correct_number = re.sub(pattern,'', phone_number) #return a string
    if correct_number.startswith('0'):
        correct_number = '+38' + correct_number
    else:
        correct_number = '+' + correct_number
    return correct_number

#git pull test test
#git fetch test test
