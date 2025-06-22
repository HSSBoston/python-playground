# Library to use OpenWeatherMap's Geocoding API
# June 16, 2025 v0.01
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/
#
# OpenWeather's Geocoding API:
#   https://openweathermap.org/api/geocoding-api
# OpenWeather's Geocoding API uses ISO 3166 country code:
#   https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
#   Examples: "US", "JP", "GB"

import requests, json

# Takes a URL (str) to call OpenWeatherMap's Geocoding API
# Returns latitude (str) and longitude (str) as a tuple
#
def getLatLon(url):
    response = requests.get(url)
    if response.status_code == 200:
        responseList = json.loads(response.text)
        if len(responseList) == 0:
            raise RuntimeError("No (lat,lon) found for a given location with OpenWeather Geocoding API")
        else:
            firstResponse = responseList[0]
            if "lat" in firstResponse and "lon" in firstResponse:
                lat = firstResponse["lat"]
                lon = firstResponse["lon"]
                return (lat, lon)
    else:
        raise RuntimeError("OpenWeather Geocoding API call error: Status code: " +
                           str(response.status_code) + response.text)

# Takes a cityName (str), US state code (str) and API key (str) to
#   call Geocoding API
# Returns latitude (str) and longitude (str) as a tuple
#
def getUsLatLon(cityName, stateCode, apiKey):
    url = "http://api.openweathermap.org/geo/1.0/direct?q=" + \
              cityName + "," + stateCode + "," + "US" + \
              "&appid=" + apiKey
    return getLatLon(url)

# Takes a cityName (str), country code (str) and API key (str) to
#   call Geocoding API
# Returns latitude (str) and longitude (str) as a tuple
#
def getIntlLatLon(cityName, countryCode, apiKey):
    url = "http://api.openweathermap.org/geo/1.0/direct?q=" + \
              cityName + ",," + countryCode + \
              "&appid=" + apiKey
    return getLatLon(url)

# Takes a zip code (str), country code (str) and API key (str) to
#   call Geocoding API
# Returns latitude (str) and longitude (str) as a tuple
#
def getZipLatLon(zipCode, countryCode, apiKey):
    url = "http://api.openweathermap.org/geo/1.0/zip?zip=" + \
              zipCode + "," + countryCode + \
              "&appid=" + apiKey
    response = requests.get(url)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "lat" in responseDict and "lon" in responseDict:
            lat = responseDict["lat"]
            lon = responseDict["lon"]
            return (lat, lon)
        else:
            raise RuntimeError("No (lat,lon) found for a given location with OpenWeather Geocoding API")            
    else:
        raise RuntimeError("OpenWeather Geocoding API call error: Status code: " +
                           str(response.status_code) + response.text)

if __name__ == "__main__":
    apiKey = ""
    print( getUsLatLon("Boston", "MA", apiKey) )
    print( getIntlLatLon("Sagamihara", "JP", apiKey) )
    print( getZipLatLon("02125", "US", apiKey) )
    print( getZipLatLon("252-0239", "JP", apiKey) )
