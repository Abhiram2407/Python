from datetime import datetime
import pytz
print("\033[1;31m]")#for red color
a=pytz.timezone("Asia/Kolkata")
b=datetime.now(a)
print(b)
for i in pytz.all_timezones:#for all timezone codes
  print(i)
