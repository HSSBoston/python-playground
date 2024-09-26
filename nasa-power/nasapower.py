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

def readNasaData(csvFileName, features):
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
# The name of an output file is formatted with startDate and endDate; e.g., nasa20240909-20240922.csv. 
#
def downloadNasaData(lat, lon, paramsToDownload, startDate, endDate):
    params = ",".join(paramsToDownload)
    fileName = "nasa" + startDate + "-" + endDate + ".csv"

    url = "https://power.larc.nasa.gov/api/temporal/daily/point?parameters=" + \
            str(params) + "&community=AG&" + \
            "longitude=" + str(lon) + "&latitude=" + str(lat) + \
            "&start=" + str(startDate) + "&end=" + str(endDate) + "&format=CSV"
    response = requests.get(url)
    if response.status_code == 200:
        open(fileName, "wb").write(response.content)
        print("Successfully downloaded data from NASA POWER. Saved it in", fileName)
    else:
        raise RuntimeError(f"Failed to download data from NASA POWER. Status code: {response.status_code}, {response.text}")

    elevation = getElevation(fileName)    
    meanFeatures = readNasaData(fileName, paramsToDownload)
    return (elevation, meanFeatures)

if __name__ == "__main__":
    cityState = "Boston, MA"
    dataToDownload = ["ALLSKY_SFC_SW_DWN", "T2M", "T2M_MAX", "TS", "TS_MAX", "PRECTOTCORR", "RH2M",
                      "GWETPROF"]
    startDate = "20230101"
    endDate   =  "20231231"
    lat, lon = cityStateToLatLon("Boston, MA")
    print(cityState, lat, lon)

    elevation, dataset = downloadNasaData(lat, lon, dataToDownload, startDate, endDate)
    print("Elevation", elevation)
    print(dataToDownload)
    print(dataset)
