# to get current date and time, i imported the datetime library
from datetime import datetime, timedelta
today = datetime.now()

print('Today is: ' + str(today))

#timedelta is used to remove or add a period of time i.e days, weeks to a date
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# empty space to keep the output result in the terminal clean
print('')

one_week = timedelta(weeks=1)
last_week = today - one_day
print('Last week was:' + str(last_week))

print("Today's Day:" + str(today.day))
print("We're currently in the month" + str(today.month))
print('Year:' + str(today.year))


