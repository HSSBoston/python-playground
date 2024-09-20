import folium, json

geoJsonFileName = "COUNTIES_POLY.json"
geoJsonFile = open(geoJsonFileName, 'r')
geoDict = json.load(geoJsonFile)

logan = (42.365792221496, -71.00966724673485)

bostonMap = folium.Map(location=logan, zoom_start=11)

folium.GeoJson(geoDict).add_to(bostonMap)

bostonMap.save("ma-counties2.html")




