from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Повертає різницю між поточною і заданою датою.
    """
    right_now = datetime.today()
    date = datetime.strptime(date, '%Y-%m-%d')
    difference = right_now - date
    return difference.days


if __name__ == "__main__":
    date_ = '2020-10-09'
    days_from_today = get_days_from_today(date_)
    print(f'Кількість днів :{days_from_today}')
