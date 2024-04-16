import re

def normalize_phone(phone_number: str) ->str:
    pattern = r"\D"
    correct_number = re.sub(pattern,'', phone_number) #return a string
    if correct_number.startswith('0'):
        correct_number = '+38' + correct_number
    else:
        correct_number = '+' + correct_number
    return correct_number