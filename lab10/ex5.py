import datetime
import calendar
import sys

years_count = int(sys.argv[1])
current_year = datetime.datetime.now().year
for i in range(0, years_count):
    year_end = str("%s %s %s" % (31, 12, current_year - i))
    old_year_end = datetime.datetime.strptime(year_end, '%d %m %Y').weekday()
    print(calendar.day_name[old_year_end])
