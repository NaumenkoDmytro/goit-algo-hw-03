'''
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.
'''
from datetime import datetime, timedelta

def date_counter(date:str):
    if type(date) != str:
        print(f"{date} - is not a string, sorry but we can work only with strings in format'YYYY-MM-DD' ")
        return 0 
    else:   
        user_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.now()
        date_difference = user_date - current_date
        return date_difference.days

print(date_counter('2020-10-09'))

