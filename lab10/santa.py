import datetime

today = datetime.date.today()
future_date = datetime.date(2019, 12, 25)

now = datetime.datetime.now()
hour = now.replace(hour=3, minute=33, second=33, microsecond=0)
seconds = (hour - now).seconds
days = (future_date - today).total_seconds() + datetime.timedelta(seconds=seconds).total_seconds()

print("%d seconds" % (days))
