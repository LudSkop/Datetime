#Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт.
# Він відповідає за відрізок часу між двома датами.
from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2024, month=5, day=1, hour=1)

difference = seventh_day_2020 - seventh_day_2019

print(difference)                   # 365 days, 0:00:00
print(difference.total_seconds())   # 31536000.