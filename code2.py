import pendulum

date = pendulum.datetime(2022, 11, 19, 20, 30, 15)

print(date.to_date_string())

print(date.to_time_string())

print(date.to_formatted_date_string())