from datetime import datetime, timezone
import pytz

pst = pytz.timezone("US/Pacific")
dtPst = datetime.now(pst)
print(dtPst)
dtUtc = dtPst.astimezone( pytz.timezone("UTC") )

print(dtPst.utcoffset())

dt =datetime(2024, 9, 1)
print(dt)
print(dt.utcoffset())
rint(dtJst.year)
print(dtJst.month)
print(dtJst.day)