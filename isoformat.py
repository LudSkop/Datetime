# Метод isoformat() використовується для перетворення об'єкта дати та часу в рядок у форматі iso.
from datetime import datetime

now = datetime.now()
iso_date_time = now.isoformat()
print(iso_date_time)
iso_date_time_timezone = now.isoformat() + now.astimezone().strftime('%z')
print(iso_date_time_timezone)
