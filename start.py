from datetime import datetime


tz = '25.05.2024'
d = datetime.strptime(tz, '%d.%m.%Y')
print(type(d))
print(f'Рік та дата : {d}')
print(f'Число : {d.day} \nРік : {d.year} \nМісяць : {d.month}')


