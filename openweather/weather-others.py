from openweather import *

weatherApiKey = ""

# Latitude and longitude of Logan airport
latitude = 42.3663
longitude = -71.0095
weatherData = getLatLonWeather(latitude, longitude, "metric", weatherApiKey)
print("Location: " + str(latitude) + ", " + str(longitude))

mainCond, description, iconId = getCurrentWeatherCondition(weatherData)
print("Weather condition: " + mainCond + ", " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (m/s): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (m/s): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))

cloudiness = getCurrentCloudiness(weatherData)
print("Cloudiness (%): " + str(cloudiness))
print("----------")


cityName = "Boston"
stateCode = "MA"
weatherData = getUsWeather(cityName, stateCode, "imperial", weatherApiKey)
print("Location: " + cityName + ", " + stateCode)

mainCond, description, iconId = getCurrentWeatherCondition(weatherData)
print("Weather condition: " + mainCond + ", " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (miles/hr): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (miles/hr): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))

cloudiness = getCurrentCloudiness(weatherData)
print("Cloudiness (%): " + str(cloudiness))
print("----------")

cityName = "Sagamihara"
countryCode = "JP"
weatherData = getIntlWeather(cityName, countryCode, "metric", weatherApiKey)
print("Location: " + cityName + ", " + countryCode)

mainCond, description, iconId = getCurrentWeatherCondition(weatherData)
print("Weather condition: " + mainCond + ", " + description)

windSpeed, windDegrees, windGust = getCurrentWind(weatherData)
print("Wind speed (m/s): " + str(windSpeed) + \
      ", Wind direction (degrees): " + str(windDegrees) + \
      ", Wind gust (m/s): " + str(windGust))

uvi = getCurrentUvi(weatherData)
print("UV Index: " + str(uvi))

pressure = getCurrentAtmosphericPressure(weatherData)
print("Atomospheric pressure (hPa): " + str(pressure))

cloudiness = getCurrentCloudiness(weatherData)
print("Cloudiness (%): " + str(cloudiness))
