from datetime import datetime,timedelta
import calendar

today = datetime.now()

print(today)
print('Today is: ' + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

print("Today's year: "+str(today.year))
print("Today's month: "+str(today.month))
print("Today's day: "+str(today.day))

birthday = input('What is your birthday (dd/mm/yyyy)?\n')
try:
    birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
    print(birthday_date)
    print(birthday_date.weekday())
    weekdays = list(calendar.day_name)
    print(weekdays[birthday_date.weekday()])
except:
    print('problem with date conversion')
finally:
    print('thats all folks')



