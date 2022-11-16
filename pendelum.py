from datetime import datetime
import time
import pendulum

datetime1 = pendulum.datetime(2022, 11, 13, tz= "America/Chicago")
print(datetime1)
print(isinstance(datetime1, datetime))

print(datetime1.timezone.name)


datetime2= datetime1.in_timezone("Europe/London")


datetime3 = pendulum.now()
print(datetime3)
print(datetime3.timezone.name)

now_in_france = pendulum.now('Europe/Paris')

print(now_in_france)
