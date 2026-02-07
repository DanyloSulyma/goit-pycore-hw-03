import random

list_numbers = []
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= quantity <= max <= 1000):
        return []
    try:
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)
    except ValueError:
        return []