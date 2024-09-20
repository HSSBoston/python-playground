import folium, json

geoJsonFileName = "COUNTIES_POLY.json"

logan = (42.365792221496, -71.00966724673485)

bostonMap = folium.Map(location=logan, zoom_start=11)

folium.GeoJson(geoJsonFileName).add_to(bostonMap)

bostonMap.save("ma-counties.html")




