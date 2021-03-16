import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

dt_str = 'March 16, 2021'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt)