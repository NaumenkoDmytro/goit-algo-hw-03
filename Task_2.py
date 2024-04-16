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