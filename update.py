
from datetime import datetime

d = datetime(year=2000, month=1, day=28,hour=17,minute=50)
print(d)
a = d.strftime('%Y.%B.%A.%H.%M')
print(a)