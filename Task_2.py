import random

list_numbers = []
def get_numbers_ticket(min, max, quantity):
    while len(list_numbers) < quantity:
        number = random.randint(min, max)
        if min > 0 and max < 1001 and quantity > 0 and quantity < 1001:
            if number not in list_numbers:
                list_numbers.append(number)
        else:
            return list_numbers
    return list_numbers