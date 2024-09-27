from datetime import datetime, timedelta

dtNow = datetime.now()
print(dtNow.hour)
print(dtNow.minute)

sleepPeriod = 60 - dtNow.minute + 3


