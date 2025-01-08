from datetime import date
from datetime import time
from datetime import datetime


d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
