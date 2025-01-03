import folium, json

geoJsonFileName = "COUNTIES_POLYM.json"

logan = (42.365792221496, -71.00966724673485)

bostonMap = folium.Map(location=logan, zoom_start=11)

folium.GeoJson(
    geoJsonFileName,
    style_function=lambda feature: {
        "weight": 2,
        "fillColor": "green"
            if feature["properties"]["COUNTY"].lower() == "middlesex"
            else "blue",
        "fillOpacity": 0.1
    },
).add_to(bostonMap)

# folium.GeoJson(
#     geoJsonFileName,
#     style_function=lambda feature: {
#         "fillColor": "#ffff00",
#         "color": "black",
#         "weight": 2,
#         "dashArray": "5, 5",
#     },
# ).add_to(bostonMap)

bostonMap.save("ma-counties.html")




