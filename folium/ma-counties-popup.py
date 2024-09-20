import folium
import folium.features

geoJsonFileName = "COUNTIES_POLYM.json"

logan = (42.365792221496, -71.00966724673485)

bostonMap = folium.Map(location=logan, zoom_start=11)


gJson= folium.GeoJson(
    geoJsonFileName,
    style_function=lambda feature: {
        "weight": 2,
        "fillColor": "green"
            if feature["properties"]["COUNTY"].lower() == "middlesex"
            else "transparent",
        "fillOpacity": 0.1,
    },
#     popup=popup,
).add_to(bostonMap)

popup = folium.features.GeoJsonPopup(
    fields=["COUNTY"],
    labels=False
).add_to(gJson)


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




