# Font choices: https://fontawesome.com/
#
# Boundarires of MA counties (shepefiles):
#   https://www.mass.gov/info-details/massgis-data-counties
#
# Shapefile -> GeoJson conversion: 
#   https://mapshaper.org/
#   https://github.com/mbloch/mapshaper/wiki/Command-Reference
#     mapshaper -proj wgs84 -simplify dp 20% -o COUNTIES_POLYM.json
#   GDAL's ogr2ogr command:
#     ogr2ogr -f GeoJSON -t_srs crs:84 COUNTIES_POLYM.geojson COUNTIES_POLYM.shp
#    
# US counties database: https://simplemaps.com/data/us-counties
#
# Style choices in folium follows CSS style properties.
#   https://www.w3schools.com/cssref/index.php
#   Font name choices (predefined names): https://www.w3.org/wiki/CSS/Properties/color/keywords
#

import folium, folium.plugins, branca
import json
from pprint import pprint

ebirdJsonFileName = "maCountyNameToRecords.json"

countyNameToRecords = {}
with open(ebirdJsonFileName, mode="r") as f:
    countyNameToRecords = json.load(f)

maCenter =        (42.4072, -71.3824)
maCountyCenters = {
    "Barnstable": (41.7244, -70.2903),
    "Berkshire":  (42.3707, -73.2063),
    "Bristol":    (41.7972, -71.1145),
    "Dukes":      (41.3961, -70.65),
    "Essex":      (42.6732, -70.9524),
    "Franklin":   (42.5831, -72.5918),
    "Hampden":    (42.1351, -72.6316),
    "Hampshire":  (42.3402, -72.6638),
    "Middlesex":  (42.4856, -71.3918),
    "Nantucket":  (41.2831, -70.0692),
    "Norfolk":    (42.1603, -71.2118),
    "Plymouth":   (41.9511, -70.8115),
    "Suffolk":    (42.3329, -71.0735),
    "Worcester":  (42.3514, -71.9077),}

maMap = folium.Map(location = maCenter, zoom_start = 7)

folium.GeoJson(
    "COUNTIES_POLYM.json",
    style_function = lambda geoJsonFeatures: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0},
).add_to(maMap)

folium.GeoJson(
    "us-states.json",
    style_function = lambda geoJsonFeatures: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0},
).add_to(maMap)

heatmapData =[]
for countyName, countyCenter in maCountyCenters.items():
    heatmapData.append( [countyCenter[0],
                         countyCenter[1],
                         countyNameToRecords[countyName]["totalObsCount"] ])
    print(countyName, countyNameToRecords[countyName]["totalObsCount"])
print(heatmapData)

folium.plugins.HeatMap(
    data = heatmapData,
    radius = 30,
).add_to(maMap)
# radius=,max_opacity=1,gradient={0.38: 'blue', 0.4: 'lime', 0.5:'yellow',0.75: 'orange', 0.9:'red'}


maMap.save("ma-heatmap.html")




