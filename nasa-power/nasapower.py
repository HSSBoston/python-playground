import requests, csv
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="spaceapps24")

# Takes "cityName, stateCode" as cityState and returns its (lat, lon).
#
def cityStateToLatLon(cityState):
    queryParams = {"city" : cityState.split(",")[0].lstrip().rstrip(),
                   "state" : cityState.split(",")[1].lstrip().rstrip(),
                   "country" : "United States" }
    location = geolocator.geocode(query=queryParams, timeout=1000)
    if location != None:
        return (location.latitude, location.longitude)
    else:
        raise RuntimeError(f"Failed to find (lat, lon) for {cityState} with Nominatim.")

def readDailyData(csvFileName, features):
    dataCount = 0
    featureSum = [0] * len(features)
    featureMissingCount = [0] * len(features)
    meanFeatures = []
    with open(csvFileName, "r") as f:
        csvReader = csv.reader(f)
        for rowindex, row in enumerate(csvReader):
            if row[0] == "YEAR":
                if row[2:] != features:
                    print("The expected parameters (features) NOT included in downloaded data.")
                    return None
                else:
                    print("Reading downloaded data.")
            if row[0].startswith("19") or row[0].startswith("20"):
                dataCount += 1
                for i, feature in enumerate(features):
                    if float( row[2+i] ) != -999:
                        featureSum[i] += float(row[2+i])
                    else:
                        featureMissingCount[i] += featureMissingCount[i]
        for i, feature in enumerate(features):
            meanFeatures.append( featureSum[i]/(dataCount-featureMissingCount[i]) )
        return meanFeatures

def getElevation(csvFileName):
    elevation = None
    with open(csvFileName, "r") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            if row[0].startswith("Elevation"):
                elevation = row[0].split("= ")[1].split(" ")[0]
        return float(elevation)

# Download data from NASA POWER and save it as a CSV file.
#   temporalResolution: "climatology", "monthly", "daily" or "hourly"
#   startDate, endDate: YYYYMMDD format (e.g. "20230101") if temporalResolution=="daily" or "hourly"
#                       YYYY format (e.g. "2023") if temporalResolution=="monthly"
#   outputFileName: output CSV file name. When omitted, the file name is formatted with
#     temporal resolution, startDate and endDate; e.g., nasa-monthly-20240909-20240922.csv. 
#
def downloadNasaData(lat: float, lon: float, temporalResolution: str, paramsToDownload: list,
                     startDate: str  = None, endDate: str  = None, outputfileName: str = None):
    assert temporalResolution in ["climatology", "monthly", "daily", "hourly"], "Wrong temporal" +\
        "resolution. It has to be 'climatology', 'monthly', 'daily' or 'hourly'."

    params = ",".join(paramsToDownload)

    if temporalResolution in ["monthly", "daily", "hourly"]:
        assert startDate != None and endDate != None, "startDate and endData must not be None when" +\
            "temporal resolution is 'monthly', 'daily' or 'hourly'."
        outputfileName = "nasa-" + temporalResolution + "-" + startDate + "-" + endDate + ".csv"
        url = "https://power.larc.nasa.gov/api/temporal/" + \
                temporalResolution + "/point?parameters=" + \
                params + "&community=AG" + "&latitude=" + str(lat) + "&longitude=" + str(lon) + \
                "&start=" + startDate + "&end=" + endDate + "&format=CSV"

    if temporalResolution == "climatology":
        assert startDate == None and endDate == None, "startDate and endData must be None when" +\
            "temporal resolution is 'climatology'."
        outputfileName = "nasa-" + temporalResolution + ".csv"
        url = "https://power.larc.nasa.gov/api/temporal/" + \
                temporalResolution + "/point?parameters=" + \
                params + "&community=AG" + "&latitude=" + str(lat) + "&longitude=" + str(lon) + \
                "&format=CSV"

    response = requests.get(url)
    if response.status_code == 200:
        open(outputfileName, "wb").write(response.content)
        print("Successfully downloaded data from NASA POWER. Saved it in", outputfileName)
    else:
        raise RuntimeError(f"Failed to download data from NASA POWER. Status code: {response.status_code}, {response.text}")    
    return outputfileName

if __name__ == "__main__":
    cityState = "Boston, MA"
    lat, lon = cityStateToLatLon("Boston, MA")
    print(cityState, lat, lon)

#     dataToDownload = ["ALLSKY_SFC_SW_DWN", "T2M", "PRECTOTCORR", "RH2M"]
#     fileName = downloadNasaData(lat, lon, "hourly", dataToDownload, "20231231", "20231231")
#     print("Downloaded data", dataToDownload)
#     print("Elevation", getElevation(fileName))

#     dataToDownload = ["ALLSKY_SFC_SW_DWN", "T2M", "T2M_MAX", "TS", "TS_MAX", "PRECTOTCORR", "RH2M",
#                       "GWETPROF"]
#     fileName = downloadNasaData(lat, lon, "daily", dataToDownload, "20231231", "20231231")
#     print("Elevation", getElevation(fileName))
#     print("Downloaded data", dataToDownload)
#     print("Mean", readDailyData(fileName, dataToDownload))

    dataToDownload = ["ALLSKY_SFC_SW_DWN", "T2M", "T2M_MAX", "TS", "TS_MAX", "PRECTOTCORR", "RH2M",
                      "PRECTOTCORR_SUM", "GWETPROF"]
    fileName = downloadNasaData(lat, lon, "monthly", dataToDownload, "1981", "2022")
    print("Elevation", getElevation(fileName))

#     fileName = downloadNasaData(lat, lon, "climatology", dataToDownload)
#     print("Elevation", getElevation(fileName))