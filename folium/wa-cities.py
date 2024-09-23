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

import folium

geoJsonFileName = "counties_wa.json"
waCenter = (47.7511, -120.7401)

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
# 
# for countyName, countyCenter in maCountyCenters.items():
#     folium.Marker(
#         countyCenter,
#         popup = folium.Popup(
#             f"<b>{countyName}</b><p>some extra info</p>",
#             show = True,
#             sticky = True,
#             ),
#     ).add_to(maMap)

waMap.save("wa-counties.html")





