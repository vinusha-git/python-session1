#to get current date and time we use datetime function
from datetime import datetime,timedelta
current_date=datetime.now()
print('year is  ' + str(current_date.year))
print('day is  ' + str(current_date.day))
print('month is  ' + str(current_date.month))
print('Today is  ' + str(current_date))
print('hour is  ' + str(current_date.hour))
print('minute is  ' + str(current_date.minute))
print('second is  ' + str(current_date.second))



#we use time delta to add remove days,weeks and year to a date
#using dates
# one_day=timedelta(days=1)
# yesterday=current_date-one_day

# tommorrow=current_date+one_day
# print('yesterday was:' +str(yesterday))
# print('tommorrow was:' +str(tommorrow))

#using month
one_week=timedelta(weeks=1)
last_week=current_date-one_week
print('last week was:'+str(last_week))

#takes date  and convert to string
birthday=input('Enter your Birthday(dd/mm/yyyy) :' )
birthday_date=datetime.strptime(birthday,'%d/%m/%Y')
print('my birthday was on :' +str(birthday_date))
one_day=birthday_date-timedelta(days=1)
print('day before my birthday:' + str(one_day))



