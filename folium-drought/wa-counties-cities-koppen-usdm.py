# Map tile choices: https://leaflet-extras.github.io/leaflet-providers/preview/
#   USGS.USTopo
#   OpenTopoMap
#   TopPlusOpen.Color
#   Stadia.StamenTerrainBackground
#   Thunderforest.Landscape
#   Jawg.Terrain
#   Esri.WorldStreetMap
#   Esri.WorldPhysical
#   NASAGIBS.ViirsEarthAtNight2012
#
# Font choices: https://fontawesome.com/
#
# Boundarires of WA counties (shepefiles/GeoJson):
#   https://geo.wa.gov/datasets/wadnr::wa-county-boundaries/
#
# Shapefiles -> GeoJson (and GeoJson -> GeoJson) conversion: 
#   https://mapshaper.org/
#     mapshaper -proj wgs84 -simplify dp 20% -o COUNTIES_POLYM.json
#   GDAL's ogr2ogr command:
#     ogr2ogr -f GeoJSON -t_srs crs:84 COUNTIES_POLYM.geojson COUNTIES_POLYM.shp
#
# Style choices in folium follows CSS style properties.
#   https://www.w3schools.com/cssref/index.php
#   Font name choices (predefined names): https://www.w3.org/wiki/CSS/Properties/color/keywords
#
# Icon color choices: 'darkgreen', 'white', 'cadetblue', 'darkred', 'darkblue', 'orange',
#   'purple', 'green', 'lightblue', 'lightgray', 'red', 'black', 'blue', 'gray', 'darkpurple',
#   'lightred', 'lightgreen', 'pink', 'beige'
#
# USDM Drought Map: https://droughtmonitor.unl.edu/DmData/GISData.aspx
#
# World Bank, Köppen-Geiger Climate Classification: https://datacatalog.worldbank.org/search/dataset/0042325

import folium
from maputils import cityStateToLatLon
from usdm import *

cluster0 = ["Seattle, WA", "Bellevue, WA", "Renton, WA"]
cluster1 = ["Issaquah, WA", "North Bend, WA"]
cluster2 = ["Easton, WA", "Cle Elum, WA"]
cluster3 = ["Quincy, WA", "George, WA", "Ritzville, WA", "Ellensburg, WA", "Sprague, WA",
            "Cheney, WA", "Spokane, WA", "Liberty Lake, WA"]
clusters = [cluster0, cluster1, cluster2, cluster3]
iconColors = ["red", "blue", "darkpurple", "pink"]

usdmFileName = downloadUsdmDroughtSeverityGeoJson("usdm_current.json")
# usdmFileName = downloadUsdmDroughtSeverityGeoJson("usdm_20240903.json")

waCenter = (47.7511, -120.7401)

waMap = folium.Map(location = waCenter, zoom_start = 8, tiles="TopPlusOpen.Color")

folium.GeoJson(
    "counties_wa.json",
    name = "County Boundaries",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillColor": "transparent"}
).add_to(waMap)

folium.GeoJson(
    "climate-classification.json",
    name = "Climate Classification",
    style_function=lambda feature: {
        "color": "darkgreen",
        "weight": 2,
        "fillColor": "yellow"   if feature["properties"]["GRIDCODE"] == 34 # Csa
                else "yellow"         if feature["properties"]["GRIDCODE"] == 35 # Csb
                else "green"         if feature["properties"]["GRIDCODE"] == 31 # Cfa
                else "green"         if feature["properties"]["GRIDCODE"] == 32 # Cfb
                else "green"         if feature["properties"]["GRIDCODE"] == 33 # Cfc
                else "orange"         if feature["properties"]["GRIDCODE"] == 26 # Bsk
                else "orange"         if feature["properties"]["GRIDCODE"] == 27 # Bsh
                else "brown"         if feature["properties"]["GRIDCODE"] == 21 # BWk
                else "brown"         if feature["properties"]["GRIDCODE"] == 22 # BWh
                else "blue"         if feature["properties"]["GRIDCODE"] == 41 # Dfa
                else "blue"         if feature["properties"]["GRIDCODE"] == 42 # Dfb
                else "blue"         if feature["properties"]["GRIDCODE"] == 43 # Dfc
                else "blue"         if feature["properties"]["GRIDCODE"] == 44 # Dfd
                else "lightgreen"         if feature["properties"]["GRIDCODE"] == 37 # Cwa
                else "lightgreen"         if feature["properties"]["GRIDCODE"] == 38 # Cwb
                else "lightgreen"         if feature["properties"]["GRIDCODE"] == 39 # Cwc
                else "transparent",
        "fillOpacity": 0.3}
).add_to(waMap)

folium.GeoJson(
    usdmFileName,
    name = "Drought Severity",
    style_function=lambda feature: {
        "color": "red",
        "weight": 1,
        "fillColor": "darkbrown"   if feature["properties"]["DM"] == 4
                else "red"         if feature["properties"]["DM"] == 3
                else "darkorange"  if feature["properties"]["DM"] == 2
                else "lightsalmon" if feature["properties"]["DM"] == 1
                else "yellow"      if feature["properties"]["DM"] == 0
                else "transparent",
        "fillOpacity": 0.3},
).add_to(waMap)

for clusterId, cluster in enumerate(clusters):
    featureGroup = folium.FeatureGroup("Cluster " + str(clusterId)).add_to(waMap)
    for city in cluster:
        cityName = city.split(",")[0]
        folium.Marker(
            cityStateToLatLon(city),
            popup = folium.Popup(
                f"<b>{cityName}</b><p>Cluster ID: {clusterId}</p>"),
            icon=folium.Icon(
                prefix = "fa",
                icon = str(clusterId), 
                color = iconColors[clusterId]),
        ).add_to(featureGroup)

folium.LayerControl().add_to(waMap)
waMap.save("wa-counties-cities-koppen-usdm.html")

