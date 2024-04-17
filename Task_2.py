'''
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.



Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
'''

import random

def get_numbers_ticket(min:int, max:int, quantity:int):
    try:
        if min < 1 or max > 1000 or max < min or quantity <1 or quantity > 1000 or quantity > max-min+1:
            print(f"Out of range")
            return list()
        else:
            return sorted(random.sample(range(min, max+1), quantity))
    except TypeError:
        print("We can work only with int type, please change it")
        return None
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)