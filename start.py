from datetime import datetime


tz = '25.05.2022'
d = datetime.strptime(tz, '%d.%m.%Y')
print(type(d))
print(f'Рік та дата : {d}')
print(f'Число : {d.day} \nРік : {d.year} \nМісяць : {d.month}')
temp_replace = d.replace(year=2024, month=8, day=16, hour=15, minute=25)
print(temp_replace)

# метод replace() повертає  новий об'єкт datetime зі зміненими   атрибутами.
