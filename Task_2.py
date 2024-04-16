'''
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.



Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
'''

import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max < min or quantity <1 or quantity > 1000 or quantity > max-min+1:
        print(f"Out of range")
        return list()
    else: 
        ticket_list = set()
        while len(ticket_list) < quantity:
            ticket_list.add(random.randint(min, max))

        print(f"The range of number starts from: {min} to {max}")
        return ticket_list
          
        

lottery_numbers = get_numbers_ticket(1, 100, 9)
print("Ваші лотерейні числа:", lottery_numbers)
print(len(lottery_numbers))