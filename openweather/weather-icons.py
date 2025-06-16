from openweather import *
from PIL import Image

weatherApiKey = ""

# Latitude and longitude of Logan airport
latitude = 42.3663
longitude = -71.0095
weatherData = getLatLonWeather(latitude, longitude, "metric", weatherApiKey)
print("Location: " + str(latitude) + ", " + str(longitude))

mainCond, description, iconId = getCurrentWeatherCondition(weatherData)
print("Weather condition: " + mainCond + ", " + description)

iconImage = getWeatherIconImage(iconId, "2x")
print("Image info: " + iconImage.format + str(iconImage.size) + iconImage.mode)
iconImage.save("downloadedWeatherIcon.png")
iconImage.show()

