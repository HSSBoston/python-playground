# Library to download WBGT (Web Bulb Globe Temperature) forecasts with
# National Digital Forecast Database (NDFD).
#
# July 28, 2024, v0.03
#
# NDFD is developed by Meteorological Development Laboratory (MDL) of
# NOAA (National Oceanic and Atmospheric Administration) for
# National Weather Service (NWS).
#   https://vlab.noaa.gov/web/mdl/home
#   https://vlab.noaa.gov/web/mdl/ndfd
#
# This library accesses to NDFD data via REST in XML (Digital Weather
# Markup Language (DWML).
#   https://digital.weather.gov/xml/rest.php
# The list of weather query parameters: 
#  https://digital.weather.gov/xml/docs/elementInputNames.php
#
# To use this library, install the xmltodict module: 
#   sudo pip3 install xmltodict

# import requests, xmltodict, os, csv, time
# from datetime import datetime, timedelta
# from pprint import pprint
# from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="spaceapps24-wbgt")

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

def downloadData(lat, lon):
    dtNow = datetime.now().replace(microsecond=0).isoformat()
    url = "https://digital.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?" +\
          "&XMLformat=DWML" +\
          "&lat=" + str(lat) +\
          "&lon=" + str(lon) +\
          "&product=time-series" +\
          "&begin=" + dtNow +\
          "&end=" + dtNow +\
          "&Unit=e" +\
          "&wbgt=wbgt" +\
          "&temp=temp" +\
          "&dew=deew" +\
          "&sky=sky" +\
          "&rh=rh" +\
          "&wspd=wspd" +\
          "&qpf=qpf"
    # e: US (English) standard
    # When "end=" is omitted in the URL, a 1-week forecast is returned. 
    # "&begin={{now().replace(microsecond=0).isoformat()}}" +\
    # "&end={{(now()+timedelta(hours=1)).replace(microsecond=0).isoformat()}}" +\

    response = requests.get(url)
    if response.status_code == 200:
        responseDict = xmltodict.parse(response.text)
        pprint(responseDict)
        return responseDict
    else:
        raise RuntimeError("Request failed. Status code: " + str(response.status_code))

# Takes "cityName, stateCode" as cityState 
#
def saveCurrentData(cityState):
    lat, lon = cityStateToLatLon(cityState)

    dtNow = datetime.now().replace(microsecond=0).isoformat()
    print(dtNow)
    responseDict = downloadData(lat, lon)
#     pprint(responseDict)
    
    timeStamp = responseDict["dwml"]["data"]["time-layout"][0]["start-valid-time"]
    date = timeStamp.split("T")[0]
    time = timeStamp.split("T")[1]
    hrEst = int(time[0:2])
    hrAdjustment = int(time.split("-")[1][0:2])
    hrLocal = hrEst - (hrAdjustment - 4)
    print("   ", date, time, hrEst, hrLocal, "data timestamp (date, time, EST hr, local hr)")
    
    cloud = int( responseDict["dwml"]["data"]["parameters"]["cloud-amount"]["value"] )
    humidity = int( responseDict["dwml"]["data"]["parameters"]["humidity"]["value"] )
    precip = float( responseDict["dwml"]["data"]["parameters"]["precipitation"]["value"] )
    
    if responseDict["dwml"]["data"]["parameters"]["temperature"][0]["@type"] == "hourly":
        temp = int( responseDict["dwml"]["data"]["parameters"]["temperature"][0]["value"] )
    else:
        print("!!! First temp data != hourly !!!")
    if responseDict["dwml"]["data"]["parameters"]["temperature"][1]["@type"] == "wet bulb globe":
        wbgt = int( responseDict["dwml"]["data"]["parameters"]["temperature"][1]["value"] )
    else:
        print("!!! Second temp data != WBGT !!!")
    
    wind = int( responseDict["dwml"]["data"]["parameters"]["wind-speed"]["value"] )
    
    csvRow = [dtNow, timeStamp, date, hrLocal, cityState, cloud, humidity, precip, temp, wbgt, wind]
    print("   ", csvRow)
    
    csvFileName = date + ".csv"
    if os.path.isfile(csvFileName):
        with open(csvFileName, "a") as f:
            writer = csv.writer(f)
            writer.writerow(csvRow)
    else:
        with open(csvFileName, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Program runtime", "Data timestamp", "Local date", "Local hr", "City",
                             "Cloud", "Humidity", "Precip", "Temp", "Wbgt", "Wind"])            
            writer.writerow(csvRow)
    

if __name__ == "__main__":    

    estCities1 = ["Boston, MA", "Bedford, MA", "Franklin, MA",  "Worcester, MA", "Springfield, MA",
                 "Hartford, CT", "New York, NY", "Albany, NY", "Providence, RI",
                 "Atlantic City, NJ", "Cape May, NJ", "Princeton, NJ", "Trenton, NJ",
                 "Philadelphia, PA", "Lancaster, PA", "Riverside, PA", "Pittsburgh, PA", "Oxford, PA", "York, PA",
                 "Derry, PA", "Bear Rocks, PA", "Breakneck, PA", "South Uniontown, PA", "Erie, PA", " Harrisburg, PA",
                 "Wilmington, DE", "Glasgow, DE", "Georgetown, DE", "Dover, DE",
                 "Berlin, MD", "Denton, MD", "Baltimore, MD", "Berlin, MD", "Edgewood, MD", "Annapolis, MD",
                 "Frederick, MD", "Hagerstown, MD",
                 "Cleveland, OH", "Columbus, OH", "Cincinnati, OH",
                 "Chicago, IL", "Springfield, IL",
                 "Detroit, MI", "Lansing, MI",
                 "Minneapolis, MN", "Saint Paul, MN",
                 "Milwaukee, WI"]
    estCities2 = ["Norfolk, VA", "Richmond, VA", "Reston, VA", "Winchester, VA", "Franklin, VA",
                 "Gloucester, VA", "Warsaw, VA", "Blacksburg, VA",
                 "Jacksonville, NC", "Wilmington, NC", "Greenville, NC", "Raleigh, NC", "Rocky Mount, NC", "Fayetteville, NC",
                 "Lumberton, NC", "Benson, NC", "South Mills, NC", "Scranton, NC", "Washington, NC", "Charlotte, NC",
                 "Charleston, SC", "Columbia, SC", "Florence, SC", "Myrtle Beach, SC",
                 "Savannah, GA", "Brunswick, GA", "Statesboro, GA", "Waycross, GA", "Atlanta, GA",
                 "Birmingham, AL", "Montgomery, AL", "Dothan, AL", "Huntsville, AL"]
    flCities = ["Jacksonville, FL", "Ocala, FL", "Weston, FL", "Orlando, FL", "Tampa, FL", "Hardee, FL", "Key West, FL",
                 "Naples, FL", "Melbourne, FL", "Palm City, FL", "Basinger, FL", "Zolfo Springs, FL", "Cornwell, FL", 
                 "Miami, FL", "Boca Raton, FL", "Sarasota, FL", "Palm Beach, FL", "Wellington, FL", "Jupiter, FL",
                 "Sugarton, FL", "Deer Park, FL", "Big Pine Key, FL", "Bay Point, FL", "Panama City Beach, FL",
                 "San Blas, FL", "White City, FL", "Port Charlotte, FL", "Cape Coral, FL", "Bonita Springs, FL",
                 "Miles City, FL", "Long Key, FL", "Duck Key, FL", "Kalamazoo, FL", "Flagler Beach, FL", "Princeton, FL"]
    cstCities = ["El Paso, TX", "Austin, TX", "San Antonio, TX", "Houston, TX", "McAllen, TX", "Dallas, TX",
                 "Corpus Christi, TX", "Port Isabel, TX", "Portland, TX", "Freeport, TX", "Edna, TX", "Amarillo, TX", 
                 "Baton Rouge, LA", "New Orleans, LA", "Monroe, LA", "Monroe, LA", "Morgan City, LA", "Slidell, LA",
                 "Gulfport, MS", "Pascagoula, MS", "Hattiesburg, MS", "Jackson, MS"]
    mstCities = ["Phoenix, AZ", "Tucson, AZ", "Flagstaff, AZ", "Yuma, AZ", "Kingman, AZ", "Sierra Vista, AZ",
                 "Graham, AZ", "Globe, AZ", "Beaver Dam, AZ", "Lake Havasu City, AZ", "Bullhead City, AZ", "Page, AZ",
                 "Mammoth, AZ", "New River, AZ", "Florence Junction, AZ", "Gila Bend, AZ", "Green Valley, AZ", "Why, AZ",
                 "Brenda, AZ", "Lake Havasu City, AZ", "Glendale, AZ", "Tempe, AZ", "Mesa, AZ", "Scottsdale, AZ",
                 "Apache Junction, AZ", "Morristown, AZ", "Kino Springs, AZ", "Carmen, AZ",
                 "Old Glory, AZ", "San Vicente, AZ", "Katherine, AZ",
                 "Deming, NM", "Lordsburg, NM", "Albuquerque, NM", "Santa Fe, NM", "Roswell, NM", "Mesita, NM",
                 "Socorro, NM", "Silver City, NM", "Las Cruces, NM", "Alamogordo, NM", "Farmington, NM", "Gallup, NM", 
                 "Denver, CO", "Grand Junction, CO", "Grand Junction, CO", "Fort Collins, CO", "Cortez, CO", "Uravan, CO",
                 "Salt Lake City, UT", "Cedar City, UT", "St. George, UT", "Halls Crossing, UT", "Moab, UT",
                 "Brendel, UT", "Ogden, UT", "Fillmore, UT", 
                 "Cheyenne, WY", "Casper, WY", "Buffalo, WY", "Sundance, WY",
                 "Boise, ID", "Twin Falls, ID", "Pocatello, ID", "Idaho Falls, ID"]
    pstCities = ["Las Vegas, NV", "Indian Springs, NV", "Carson City, NV", "Reno, NV", "Mesquite, NV", "Dry Lake, NV",
                 "Caliente, NV", "Beatty, NV", "Panaca, NV", "Cal-Nev-Ari, NV", "Nelson, NV", "Whitney, NV", "Elko, NV",
                 "Carson City, NV",
                 "San Diego, CA", "El Centro, CA", "Borrego Springs, CA", "Salton City, CA", "San Diego, CA", "Blythe, CA",
                 "Sky Valley, CA", "Indio, CA", "Riverside, CA",  "Anaheim, CA", "Barstow, CA", "Baker, CA",
                 "Victorville, CA", "Riverside, CA", "Ridgecrest, CA", "Lancaster, CA", "Palmdale, CA", "Twentynine Palms, CA",
                 "Los Angeles , CA", "Bakersfield, CA", "Kernville, CA", "Santa Nella, CA", "Soledad, CA", "San Jose, CA",
                 "Los Banos, CA", "Merced, CA", "Concord, CA", "Modesto, CA",  "San Francisco, CA", "Sacramento, CA",
                 "Ukiah, CA", "Yuba City, CA", "Riverside, CA", "Chico, CA", "Willows, CA", "Red Bluff, CA",
                 "Boulder, CA", "Brawley, CA", "Trona, CA", "Rock Creek, CA", "Ukiah, CA", "Fresno, CA", "Klinefelter, CA", 
                 "Borrego Springs, CA", "Redding, CA", "Weaverville, CA", "Hillcrest, CA", "Sims, CA", "Coffee Creek, CA",
                 "Lyman Springs, CA", "Yellowjacket, CA", "San Rafael, CA", "Palo Alto, CA", "Sunnyvale, CA",
                 "Santa Clara, CA", "Benicia, CA", "Antioch, CA", "Rio Vista, CA", "Napa, CA"]
    nwCities =["Seattle, WA", "Olympia, WA", "Tacoma, WA", "Yakima, WA",
               "Portland, OR", "Salem, OR", "Albany, OR", "Eugene, OR", "Medford, OR", "Bend, OR"]
    hawaiiCities = ["Honolulu, HI", "Koloa, HI", "Kihei, HI", "Hilo, HI", "Koloa, HI"]

    regions = [estCities1, estCities2, flCities, cstCities, mstCities, pstCities, nwCities, hawaiiCities]
#     regions = [flCities, cstCities, mstCities, pstCities, nwCities, hawaiiCities]

    print(len(regions))
          
#     for city in hawaiiCities:
#         saveCurrentData(city)

dtNow = datetime.now()

# while dtNow.hour <= 30:
#     for region in regions:
#         for city in region:
#             saveCurrentData(city)
#         print("Sleeping for 4 mins...")
#         time.sleep(240)
#     dtNow = datetime.now()
#     sleepMin = 60 - dtNow.minute + 3
#     print(f"Sleeping for {sleepMin} mins...")
#     time.sleep(sleepMin * 60)

