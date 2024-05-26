from  datetime import datetime


date = datetime.now()
print(f'Час в секундах з початку епохи:{date.timestamp()}')


hour = 1716758017.135023
hour_now = datetime.fromtimestamp(hour)
print(hour_now)
str_hour_now = hour_now.strftime('%d-%m-%Y, %H:%M:%S')
print(str_hour_now)
