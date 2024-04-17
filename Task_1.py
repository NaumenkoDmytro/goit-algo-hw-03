'''
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.
'''
from datetime import datetime, timedelta


# Updated Option 

def get_days_from_today(date:str):
    current_date = datetime.now()
    try:
        user_date = datetime.strptime(date, "%Y-%m-%d")
        date_difference = current_date - user_date 
        return date_difference.days
    except ValueError:
        print(f"{date} - is not a string, sorry but we can work only with string in format'YYYY-MM-DD' ")
        return None
    except TypeError:
        print(f"{date} - is not a string, sorry but we can work only with string in format'YYYY-MM-DD' ")
        return None  

print(get_days_from_today('2024-04-17'))

# #1st option
# def date_counter(date:str):
#     if type(date) != str:
#         print(f"{date} - is not a string, sorry but we can work only with string in format'YYYY-MM-DD' ")
#         return None 
#     else:   
#         user_date = datetime.strptime(date, "%Y-%m-%d")
#         current_date = datetime.now()
#         date_difference = current_date - user_date 
#         return date_difference.days

# print(date_counter('2020-10-09'))

