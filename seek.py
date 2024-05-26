# Щоб створити об'єкт datetime з будь-якою датою.
from datetime import datetime
# d1 = datetime(year=2012, month=1, day=7, hour=14)
# print(d1) # 2012-01-07 14:00:00
def get_birthday():
    date = input(f'Введіть рік.місяць.день свого дня народження:  ')
    result = datetime.strptime(date, '%Y.%m.%d')
    month_day = result.strftime('%B.%A')
    print(month_day)


if __name__ == "__main__":
    get_birthday()
