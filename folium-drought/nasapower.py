import requests, csv

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
        print("Successfully downloaded data from NASA POWER. Saved it in ", fileName)
    else:
        print("Failed to download data from NASA POWER", response.status_code)
        print(response.text)
        return (None, None)

    elevation = getElevation(fileName)    
    meanFeatures = readNasaData(fileName, paramsToDownload)
    return (elevation, meanFeatures)
