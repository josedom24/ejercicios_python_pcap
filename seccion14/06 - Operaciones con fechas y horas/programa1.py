from datetime import date
from datetime import datetime

# Resta de dos objetos 'date'
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)

# Resta de dos objetos 'datetime'
dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)
