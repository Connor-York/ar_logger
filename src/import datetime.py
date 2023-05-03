import datetime

current_time = datetime.datetime.now()
current_date = datetime.date.today()

formatted_time = current_time.strftime("%H:%M:%S")
formatted_date = current_date.strftime("%Y-%m-%d")

print("Current time is:", formatted_time)
print("Current date is:", formatted_date)
