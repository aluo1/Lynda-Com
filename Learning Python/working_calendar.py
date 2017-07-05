import calendar

''' 
# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)

print (c.formatmonth(2017, 6, 0, 0))

# print all months' name
for name in calendar.month_name:
	print (name)

# print all days' name
for name in calendar.day_name:
	print (name)
'''

# iterate through all 12 months in a year
for m in range(1,13):
	# represent an array of weeks that represent the month
	cal = calendar.monthcalendar(2017, m)
	week_one = cal[0]
	week_two = cal[1]

	print (week_one[calendar.FRIDAY]) 
	print (calendar.TextCalendar(calendar.SUNDAY).formatmonth(2017, m, 0, 0))

	if week_one[calendar.FRIDAY] != 0:
		meet_day = week_one[calendar.FRIDAY]
	else:
		# if the first friday isn't the first week, it must be the second
		meet_day = week_two[calendar.FRIDAY]

	print ("%10s %2d " % (calendar.month_name[m], meet_day))
