from openweather import *

weatherApiKey = "1e8916214f329eb63fe4956810360e09" 

cityName = "Boston"
stateCode = "MA"
weatherData = getUsWeather(cityName, stateCode, "imperial", weatherApiKey)
print(cityName + ", " + stateCode)
print(weatherData)

daytimeTemp, minTemp, maxTemp, avgHumidity = getTempHumidityToday(weatherData)
print("Forecast Today: Daytime temp (F): " + str(daytimeTemp) + ", Min temp (F): " + str(minTemp) + \
      ", Max temp (F): " + str(maxTemp) + ", Avg humidity (%): " + str(avgHumidity))

daytimeTemp, minTemp, maxTemp, avgHumidity = getTempHumidityTomorrow(weatherData)
print("Forecast Tomorrow: Daytime temp (F): " + str(daytimeTemp) + ", Min temp (F): " + str(minTemp) + \
      ", Max temp (F): " + str(maxTemp) + ", Avg humidity (%): " + str(avgHumidity))

daytimeTemp, minTemp, maxTemp, avgHumidity = getTempHumidityForecast(weatherData, 2)
print("Forecast 2 Day Later: Daytime temp (F): " + str(daytimeTemp) + ", Min temp (F): " + str(minTemp) + \
      ", Max temp (F): " + str(maxTemp) + ", Avg humidity (%): " + str(avgHumidity))
print("----------")

morningTemp, dayTemp, eveningTemp, nightTemp = getFeelsLikeToday(weatherData)
print("Forecast Today: Morning feels-like (F): " + str(morningTemp) + \
      ", Daytime feelsl-like (F): " + str(dayTemp) + ", Evening feels-like (F): " + str(eveningTemp) + \
      ", Night feels-like (F): " + str(nightTemp))

morningTemp, dayTemp, eveningTemp, nightTemp = getFeelsLikeTomorrow(weatherData)
print("Forecast Tomorrow: Morning feels-like (F): " + str(morningTemp) + \
      ", Daytime feelsl-like (F): " + str(dayTemp) + ", Evening feels-like (F): " + str(eveningTemp) + \
      ", Night feels-like (F): " + str(nightTemp))

morningTemp, dayTemp, eveningTemp, nightTemp = getFeelsLikeForecast(weatherData, 2)
print("Forecast 2 Days Later: Morning feels-like (F): " + str(morningTemp) + \
      ", Daytime feelsl-like (F): " + str(dayTemp) + ", Evening feels-like (F): " + str(eveningTemp) + \
      ", Night feels-like (F): " + str(nightTemp))
print("----------")

oneWordCond, detailedCond, iconId = getWeatherConditionToday(weatherData)
print("Forecast Today: " + oneWordCond + ", " + detailedCond)

oneWordCond, detailedCond, iconId = getWeatherConditionTomorrow(weatherData)
print("Forecast Tomorrow: " + oneWordCond + ", " + detailedCond)

oneWordCond, detailedCond, iconId = getWeatherConditionForecast(weatherData, 2)
print("Forecast 2 Days Later: " + oneWordCond + ", " + detailedCond)
print("----------")

cloudiness = getCloudinessToday(weatherData)
print("Forecast Today: Cloudiness (%): " + str(cloudiness))

cloudiness = getCloudinessTomorrow(weatherData)
print("Forecast Tomorrow: Cloudiness (%): " + str(cloudiness))

cloudiness = getCloudinessForecast(weatherData, 2)
print("Forecast 2 Days Later: Cloudiness (%): " + str(cloudiness))
