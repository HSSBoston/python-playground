from openweather import *

weatherApiKey = "" 

# Latitude and longitude of Logan airport
latitude = 42.3663
longitude = -71.0095

weatherData = getLatLonWeather(latitude, longitude, "imperial", weatherApiKey)

temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)

print("Latitude: " + str(latitude) + ", Longitude: " + str(longitude))
print("Temp (F): " + str(temp) + ", Feels like (F): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

cityName = "Boston"
stateCode = "MA"
weatherData = getUsWeather(cityName, stateCode, "metric", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(cityName + ", " + stateCode)
print("Temp (C): " + str(temp) + ", Feels like (C): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

zipCode = "02125"
countryCode = "US"
weatherData = getZipWeather(zipCode, countryCode, "imperial", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(zipCode + ", " + countryCode)
print("Temp (F): " + str(temp) + ", Feels like (F): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

cityName = "Sagamihara"
countryCode = "JP"
weatherData = getIntlWeather(cityName, countryCode, "metric", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(cityName + ", " + countryCode)
print("Temp (C): " + str(temp) + ", Feels like (C): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")

zipCode = "194-0013"
countryCode = "JP"
weatherData = getZipWeather(zipCode, countryCode, "metric", weatherApiKey)
temp, feelsLike, humidity = getCurrentTempHumidity(weatherData)
print(zipCode + ", " + countryCode)
print("Temp (C): " + str(temp) + ", Feels like (C): " + str(feelsLike) + \
      ", Humidity (%): " + str(humidity))
print("----------")
