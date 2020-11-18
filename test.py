from datetime import datetime
from datetime import timedelta
args= ['2020-10-01']
day_daignosed = datetime.strptime(args[0], '%Y-%m-%d')
# print(day_daignosed)
# print(day_daignosed.day)
# print(day_daignosed.date())
# print(day_daignosed.time())
# print(day_daignosed.weekday())
# print(day_daignosed.ctime())
# print(day_daignosed.today())

# day_daignosed = day_daignosed.day - 1
# print(day_daignosed)
one_day=timedelta(days=1)
day_daignosed =day_daignosed - one_day
print(day_daignosed)