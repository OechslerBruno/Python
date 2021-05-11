from datetime import datetime, timedelta

today = datetime.now()
print(str(today))

#Timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print(one_day)
print('yesterday was ' + str(yesterday))

#string to datetime
birthday = input("When is your birthday: ")
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

#day, month, year, hour, minute, second functions
#all theses functions return integers
print('Day...: ' + str(today.day))
print('Month.: ' + str(today.month))
print('Year..: ' + str(today.year))
print('Hour..: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))