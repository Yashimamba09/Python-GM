import datetime
current_time = datetime.datetime.now()
print("The current date and time is:", current_time.strftime("%m-%d-%y %H:%M:%S"))
print("The current day of the week is", current_time.weekday())  
print("The day of the week is:", current_time.strftime("%A"))