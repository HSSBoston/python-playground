from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
from dateutil.relativedelta import relativedelta

API_KEY = "AIzaSyCK-9MeJ0kZgSm5sCJzsv9qZNBrt5yo5Tg"
CALENDAR_ID = "44b4894cb924ae13d3d8cb33eeaf7efddf758d20b7b74dcfc88213f6b1dc3c35@group.calendar.google.com"

def getEvents(calId, apiKey, startTime, endTime):
    try:
        service = build("calendar", "v3", developerKey=apiKey)
        response = service.events().list(
            calendarId=calId,
            timeMin=startTime.isoformat() + "Z",
            timeMax=endTime.isoformat() + "Z",
            singleEvents=True,
            orderBy="startTime").execute()
        return response.get("items", [])
    except HttpError as error:
        print(error)

now = datetime.datetime.now()
today0am   = now + relativedelta(hour=0, minute=0)
tomorow0am = now + relativedelta(days=+1, hour=0, minute=0)

events = getEvents(CALENDAR_ID, API_KEY, today0am, tomorow0am)
#     print(events)

if len(events) != 0:
    for event in events:
        start = event["start"]["dateTime"]
        end   = event["end"]["dateTime"]
        evName = event["summary"]
        print(start, end, evName)
else:
    print("No events today")
