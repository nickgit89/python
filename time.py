import datetime

now = datetime.today()

print(now.strftime("%a %A %d"))

testDate = now + timedelta(days=2)