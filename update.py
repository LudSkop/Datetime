
from datetime import datetime,timedelta

d = datetime(year=2000, month=1, day=28,hour=17,minute=50)
print(d)
a = d.strftime('%Y.%B.%A.%H.%M')
print(a)
now = datetime.now()
interval = timedelta(days=10)
result_date = now - interval
print(result_date)

interval = timedelta(days=20)
result_date = now + interval
print(result_date)
