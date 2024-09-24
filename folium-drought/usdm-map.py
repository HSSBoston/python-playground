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

import folium
from usdm import *

usdmFileName = downloadUsdmDroughtSeverityGeoJson("usdm_current.json")
# usdmFileName = downloadUsdmDroughtSeverityGeoJson("usdm_20240903.json")

waCenter = (47.7511, -120.7401)

waMap = folium.Map(location = waCenter, zoom_start = 8, tiles="TopPlusOpen.Color")

folium.GeoJson(
    usdmFileName,
    name = "US Drought Monitor",
    style_function=lambda feature: {
        "color": "red",
        "weight": 1,
        "fillColor": "darkbrown"   if feature["properties"]["DM"] == 4
                else "red"         if feature["properties"]["DM"] == 3
                else "darkorange"  if feature["properties"]["DM"] == 2
                else "lightsalmon" if feature["properties"]["DM"] == 1
                else "yellow"      if feature["properties"]["DM"] == 0
                else "transparent",
        "fillOpacity": 0.3,
    },
).add_to(waMap)

waMap.save("wa-usdm.html")






