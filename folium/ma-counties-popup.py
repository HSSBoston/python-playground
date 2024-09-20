import folium
import folium.features

geoJsonFileName = "COUNTIES_POLYM.json"

maCenter = (42.4072, -71.3824)
bostonMap = folium.Map(location=maCenter, zoom_start=9)


gJson= folium.GeoJson(
    geoJsonFileName,
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillColor": "lightblue"
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




