from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print("Today's date is", today)

print("Date components", today.day, today.month, today.year)
print("Today's weekday # is", today.weekday())
days= ["mon", "tue", "wed", "thur"]
print("Which is a ", days[today.weekday()])