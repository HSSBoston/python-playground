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
#   https://geo.wa.gov/datasets/wadnr::wa-county-boundaries/about
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

import folium
from maputils import cityStateToLatLon

geoJsonFileName = "counties_wa.json"
waCenter = (47.7511, -120.7401)

cluster0 = ["Seattle, WA", "Bellevue, WA", "Renton, WA"]
cluster1 = ["Issaquah, WA", "North Bend, WA"]
cluster2 = ["Easton, WA", "Cle Elum, WA"]
cluster3 = ["Quincy, WA", "George, WA", "Ritzville, WA", "Ellensburg, WA", "Sprague, WA",
            "Cheney, WA", "Spokane, WA", "Liberty Lake, WA"]
clusters = [cluster1, cluster2, cluster3, cluster4]

waMap = folium.Map(location = waCenter, zoom_start = 8, tiles="TopPlusOpen.Color")

waCountiesLayer = folium.GeoJson(
    geoJsonFileName,
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillColor": "transparent",
#         "fillColor": "lightblue"
#             if feature["properties"]["COUNTY"] == "Middlesex"
#             else "transparent",
#         "fillOpacity": 0.1,
    },
).add_to(waMap)

for clusterId, cluster in enumerate(clusters):
    for city in cluster:
        folium.Marker(
            cityStateToLatLon(city),
            popup = folium.Popup(
                f"<b>{city.split(",")[0]}</b><p>Cluster ID: {clusterId}</p>",
                ),
        ).add_to(waMap)

waMap.save("wa-counties.html")





