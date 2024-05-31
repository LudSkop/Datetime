import random


def get_numbers_ticket(min_: int, max_: int, quantity: int) -> list[int, int] | str:
    """
    Генерація випадкових чисел для лотереї.

    """

    if isinstance(min_, int) and isinstance(max_, int) and quantity > 0:
        print('Валідація типів успішна')
        random_ = list(range(min_, max_))
        result = random.sample(random_, k=quantity)
        result.sort()
        return result
    else:
        return 'не коректні дані'


if __name__ == "__main__":
    try:
        ticket_number = get_numbers_ticket(1, 90, int(input('Введіть кількість: ')))
    except Exception:
        print('не коректно')
    print(ticket_number)
