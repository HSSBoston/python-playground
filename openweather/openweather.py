# Library to use OpenWeatherMap One Call API 3.0
# June 16, 2025 v0.01
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/
#
# OpenWeather's One Call API 3.0:
#   https://openweathermap.org/api/one-call-3
# As for weather conditions ("id", "main", "description" and "icon"), see:
#   https://openweathermap.org/weather-conditions

import requests, json, openweather_geocoding, openweather_extractors
from PIL import Image
from io import BytesIO
# from geopy.geocoders import Nominatim
# 
# nominatimAppName = "iot" + os.uname()[1]
# geolocator = Nominatim(user_agent=nominatimAppName)

# Takes lat (str), lon (str), API key (str) to call OpenWeather's API
# Returns JSON weather data (dict)
#   Optional inputs: unit
#     "imperial", "metric" or "standard"
#   Optional inputs: exclude
#     Comma-delimited list of "current", "minutely", "hourly", "daily" and "alerts"
#
def getLatLonWeather(lat, lon, apiKey, unit="imperial", exclude=""):
    assert unit in ["imperial", "metric", "standard"], "Invalid unit"
    
    url = "https://api.openweathermap.org/data/3.0/onecall?" + \
              "lat="      + str(lat) + \
              "&lon="     + str(lon) + \
              "&appid="   + apiKey + \
              "&units="   + unit + \
              "&exclude=" + exclude
    response = requests.get(url)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        return responseDict
    else:
        raise RuntimeError("OpenWeather API call error. Status code: " +
                           str(response.status_code) + response.text)

# Takes a cityName (str), US state code (str) and API key (str) to
#   call OpenWeatherMap API
# Returns JSON weather data (dict)
# 
def getUsWeather(cityName, stateCode, apiKey, unit="imperial", exclude=""):
    try:
        lat, lon = openweather_geocoding.getUsLatLon(cityName, stateCode, apiKey)
        return getLatLonWeather(lat, lon, apiKey, unit, exclude)
    except RuntimeError:
        raise        

# Takes a cityName (str), country code (str) and API key (str) to
#   call OpenWeatherMap API
# Returns JSON weather data (dict)
# 
def getIntlWeather(cityName, countryCode, apiKey, unit, exclude=""):
    try:
        lat, lon = openweather_geocoding.getIntlLatLon(cityName, countryCode, apiKey)
        return getLatLonWeather(lat, lon, apiKey, unit, exclude)
    except RuntimeError:
        raise        

# Takes a zip code (str), country code (str) and API key (str) to
#   call OpenWeatherMap API
# Returns JSON weather data (dict)
# 
def getZipWeather(zipCode, countryCode, apiKey, unit="imperial", exclude=""):
    try:
        lat, lon = openweather_geocoding.getZipLatLon(zipCode, countryCode, apiKey)
        return getLatLonWeather(lat, lon, apiKey, unit, exclude)
    except RuntimeError:
        raise        

# Takes downloaded JSON weather data (dict)
# Returns the current temp (float), feelsLike (float), humidity (float) as a tuple
#
def getCurrentTempHumidity(weatherDataDict):
    if "current" in weatherDataDict:
        return openweather_extractors.extractTempHumidity( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the current UV Index (float)
#
def getCurrentUvi(weatherDataDict): 
    if "current" in weatherDataDict:
            return openweather_extractors.extractUvi( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the current precip (float) in mm/hr. 
#
def getCurrentRain(weatherDataDict):
    if "current" in weatherDataDict:
        return openweather_extractors.extractRain( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the current precip (float) in mm/hr. 
#
def getCurrentSnow(weatherDataDict): 
    if "current" in weatherDataDict:
        return openweather_extractors.extractSnow( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the current wind speed (float, meters/miles per hr),
#   wind direction (float, degrees) and wind gust (float, meters/miles per hr)
#   as a tuple. 
#
def getCurrentWind(weatherDataDict): 
    if "current" in weatherDataDict:
        return openweather_extractors.extractWind( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the current weather ID (int), condition main name (str), 
#   condition sub name (str) and icon ID (str) as a tuple. 
#
def getCurrentWeatherCondition(weatherDataDict):
    if "current" in weatherDataDict:
        return openweather_extractors.extractWeatherCond( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes weather icon ID (str) and icon size (str)
# Returns a PNG image data for the requested icon. 
#
def getWeatherIconImage(iconId, size):
    assert type(iconId)==str, "Icon ID must be a string."
    assert size in ["2x", "4x"], "Icon size must be '2x' or '4x'" 

    url = "http://openweathermap.org/img/wn/" + \
              iconId + "@" + size +".png"
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        if image != None:
            return image
        else:
            raise RuntimeError("Donwnloaded icon not valid.")
    else:
        raise RuntimeError("Icon download failed. Status code: " + str(response.status_code))

# Takes downloaded JSON weather data (dict)
# Returns the current atmospheric pressure on the sea level, hPa (float).
#
def getCurrentAtmosphericPressure(weatherDataDict):
    if "current" in weatherDataDict:
        return openweather_extractors.extractAtmosphericPressure( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the current cloud cover (%) as an int. 
#
def getCurrentCloudCover(weatherDataDict):
    if "current" in weatherDataDict:
        return openweather_extractors.extractCloudCover( weatherDataDict["current"] )
    else:
        raise RuntimeError("Current weather data not found.")

# Takes downloaded JSON weather data (dict)
# Returns the UV Index in the next hour (float)
#
def getUviNextHr(weatherDataDict):
    if "hourly" in weatherDataDict:
        return openweather_extractors.extractUvi( weatherDataDict["hourly"][0] )
    else:
        raise RuntimeError("Data not found for the next hour.")

# Takes downloaded JSON weather data (dict)
# Returns the prob of precip (float: [0,1]) for the next hour.
#
def getProbPrecipNextHr(weatherDataDict):
    if "hourly" in weatherDataDict:
        return openweather_extractors.extractProbPrecip( weatherDataDict["hourly"][0] )
    else:
        raise RuntimeError("Data not found for the next hour.")

# Takes downloaded JSON weather data (dict)
# Returns the precip (float) for the next hour (in mm/hr). 
#
def getRainNextHr(weatherDataDict):
    if "hourly" in weatherDataDict:
        return openweather_extractors.extractRain( weatherDataDict["hourly"][0] )
    else:
        raise RuntimeError("Data not found for the next hour.")

# Takes downloaded JSON weather data (dict)
# Returns the weather ID (int), condition main name (str), 
#   condition sub name (str) and icon ID (str) for the next hour as a tuple. 
#
def getWeatherConditionNextHr(weatherDataDict):
    if "hourly" in weatherDataDict:
        return openweather_extractors.extractWeatherCond( weatherDataDict["hourly"][0] )
    else:
        raise RuntimeError("Data not found for the next hour.")






def getTempHumidityToday(response):
    return getTempHumidityForecast(response, 0)

def getTempHumidityTomorrow(response):
    return getTempHumidityForecast(response, 1)

def getTempHumidityForecast(response, daysLater):
    if response == None:
        return (None, None, None, None)
    if response.status_code == 200:
        print(response.text)
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            dayTemp = forecast["temp"]["day"]
            minTemp = forecast["temp"]["min"]
            maxTemp = forecast["temp"]["max"]
            humidity = forecast["humidity"]
            return (dayTemp, minTemp, maxTemp, humidity)
        else:
            return (None, None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None, None)

def getFeelsLikeToday(response):
    return getFeelsLikeForecast(response, 0)

def getFeelsLikeTomorrow(response):
    return getFeelsLikeForecast(response, 1)

def getFeelsLikeForecast(response, daysLater):
    if response == None:
        return (None, None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            morningTemp = forecast["feels_like"]["morn"]
            dayTemp = forecast["feels_like"]["day"]
            eveTemp = forecast["feels_like"]["eve"]
            nightTemp = forecast["feels_like"]["night"]
            return (morningTemp, dayTemp, eveTemp, nightTemp)
        else:
            return (None, None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None, None)

def getWeatherConditionToday(response):
    return getWeatherConditionForecast(response, 0)

def getWeatherConditionTomorrow(response):
    return getWeatherConditionForecast(response, 1)

def getWeatherConditionForecast(response, daysLater):
    if response == None:
        return (None, None, None)
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            weather = forecast["weather"][0]
            main = weather["main"]
            description = weather["description"]
            iconId = weather["icon"]
            return (main, description, iconId)
        else:
            return (None, None, None)
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return (None, None, None)

def getCloudinessToday(response):
    return getCloudinessForecast(response, 0)

def getCloudinessTomorrow(response):
    return getCloudinessForecast(response, 1)

def getCloudinessForecast(response, daysLater):
    if response == None:
        return None
    if daysLater > 5:
        return None
    if response.status_code == 200:
        responseDict = json.loads(response.text)
        if "daily" in responseDict:
            forecast = responseDict["daily"][daysLater]
            cloudiness = forecast["clouds"]
            return cloudiness
        else:
            return None
    else:
        print("OpenWeather Response Error. Status code: " + str(response.status_code))
        return None



# def getUsCityWeather(cityName, stateCode, unit, apiKey):
#     structuredQuery = {"city" : cityName,
#                        "state" : stateCode,
#                        "country" : "United States"}
#     location = geolocator.geocode(query=structuredQuery)
#     locationDataset = location.raw
#     return getLatLonWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)
# 
# 
# def getUsTownWeather(townName, stateCode, unit, apiKey):
#     structuredQuery = {"town" : townName,
#                        "state" : stateCode,
#                        "country" : "United States"}
#     location = geolocator.geocode(query=structuredQuery)
#     locationDataset = location.raw
#     return getLatLonWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)
# 
# def getIntlCityWeather(cityName, countryCode, unit, apiKey):
#     structuredQuery = {"city" : cityName,
#                        "country" : countryCode}
#     location = geolocator.geocode(query=structuredQuery)
#     locationDataset = location.raw
#     return getLatLonWeather(locationDataset["lat"], locationDataset["lon"], unit, apiKey)

if __name__ == "__main__":
    apiKey = ""
    lat = 42.36
    lon = -71.00
    weatherData = getLatLonWeather(lat, lon, apiKey)
    print( weatherData )
    print( getUsWeather("Boston", "MA", apiKey) )
    print( getIntlWeather("Sagamihara", "JP", apiKey, unit="metric") )
    print( getZipWeather("02125", "US", apiKey) )
    print( getZipWeather("252-0239", "JP", apiKey, unit="metric") )
           
    print("Current temp, feels-like and humidity:", getCurrentTempHumidity(weatherData))
    print("Current UVI:",                  getCurrentUvi(weatherData))
    print("Current rain:",                 getCurrentRain(weatherData))
    print("Current snow:",                 getCurrentSnow(weatherData))
    print("Current wind:",                 getCurrentWind(weatherData))
    print("Current weather condition:",    getCurrentWeatherCondition(weatherData))
    print("Current weather icon:",         getWeatherIconImage("01d", "2x"))
    print("Current atmospheric pressure:", getCurrentAtmosphericPressure(weatherData))
    print("Current cloud cover:",          getCurrentCloudCover(weatherData))

    print("Next hr UVI:",                getUviNextHr(weatherData))
    print("Next hr precip probability:", getProbPrecipNextHr(weatherData))
    print("Next hr rain:",               getRainNextHr(weatherData))    
    print("Next hr weather condition:",  getWeatherConditionNextHr(weatherData))
           