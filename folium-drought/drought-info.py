#ALLSKY_SFC_SW_DWN  CERES SYN1deg All Sky Surface Shortwave Downward Irradiance (MJ/m^2/day)
# T2M               MERRA-2 Temperature at 2 Meters (C) 
# T2M_MAX           MERRA-2 Temperature at 2 Meters Maximum (C) 
# TS                MERRA-2 Earth Skin Temperature (C) 
# TS_MAX            MERRA-2 Earth Skin Temperature Maximum (C) 
# PRECTOTCORR       MERRA-2 Precipitation Corrected (mm/day) 
# RH2M              MERRA-2 Relative Humidity at 2 Meters (%)
# GWETROOT          Root Zone Soil Wetness
# GWETTOP           Surface Soil Wetness, 
# See https://power.larc.nasa.gov/#resources for all available data.

from datetime import datetime, timedelta
from nasapower import *
from usdm import *
from usstates import *

lat = 42.36575749436916
lon = -71.00974304515053
city = "Boston"
stateCode = "MA"

dataToDownload = ["ALLSKY_SFC_SW_DWN", "T2M", "T2M_MAX", "TS", "TS_MAX", "PRECTOTCORR", "RH2M",
                  "GWETTOP"]

def getPastDate(daysAgo):
    doubleDigitMonth = doubleDigitDay = "00"
    today = datetime.now()
    dt = today - timedelta(days=daysAgo)
    if dt.month // 10 == 0:
        doubleDigitMonth = "0" + str(dt.month)
    else:
        doubleDigitMonth = str(dt.month)
    if dt.day // 10 == 0:
        doubleDigitDay = "0" + str(dt.day)
    else:
        doubleDigitDay = str(dt.day)
    return str(dt.year) + doubleDigitMonth + doubleDigitDay

# YYYYMMDD format
yesterday = getPastDate(1)
daysAgo14 = getPastDate(14)

elevation, dataset1 = downloadNasaData(lat, lon, dataToDownload, daysAgo14, yesterday)
# print(dataToDownload)
# print(dataset1)
irradiance = round(dataset1[0], 1)
airTemp = round(dataset1[2], 1)
surfaceTemp = round(dataset1[4], 1)
precip = round(dataset1[5], 1)
humidity = round(dataset1[6])
soilMoisture = round(dataset1[7]*100)

severityIndex = downloadUsdmData(city, stateCode, daysAgo14, yesterday)
severityDescription = ["Abnormally Dry", "Moderate Drought",
                       "Severe Drought", "Extreme Drought", "Exceptional Drought"]

print("Current Dounght Severity Index (0-4): ", severityIndex, severityDescription[severityIndex])
print("Daily average in the past 2 wks:")
print("Irradiance (MJ/m^2/day): ", irradiance)
print("Temperature at 2 Meters Maximum (C): ", airTemp)
print("Earth Skin Temperature Maximum (C): ", surfaceTemp)
print("Precip (mm/day): ", precip)
print("Humidity (%): ", humidity)
print("Soil Moisture (%): ", soilMoisture)



