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
# Icon color choices: 'darkgreen', 'white', 'cadetblue', 'darkred', 'darkblue', 'orange',
#   'purple', 'green', 'lightblue', 'lightgray', 'red', 'black', 'blue', 'gray', 'darkpurple',
#   'lightred', 'lightgreen', 'pink', 'beige'
#
# US Drought Monitor (USDM)
#   https://droughtmonitor.unl.edu/DmData/GISData.aspx
# North American Drought Monitor (NADM) 
#   https://droughtmonitor.unl.edu/NADM/
#   https://www.ncei.noaa.gov/access/monitoring/nadm/
# Canadian Drount Monitor (CDM)
#   https://agriculture.canada.ca/en/agricultural-production/weather/canadian-drought-monitor
# Mexico Drougt Monitor (MDM)
#   https://smn.conagua.gob.mx/es/climatologia/monitor-de-sequia/monitor-de-sequia-en-mexico

import folium
from maputils import *
from usdm import *

# These are the 4 clusters that were made for Space Apps 23. 
# cluster0 = ["Seattle, WA", "Bellevue, WA", "Renton, WA"]
# cluster1 = ["Issaquah, WA", "North Bend, WA"]
# cluster2 = ["Easton, WA", "Cle Elum, WA"]
# cluster3 = ["Quincy, WA", "George, WA", "Ritzville, WA", "Ellensburg, WA", "Sprague, WA",
#             "Cheney, WA", "Spokane, WA", "Liberty Lake, WA"]

cluster1 = ['Olympia, WA',
     "Wa'atch, WA",
     'Forks, WA',
     'James Island, WA',
     'Abbey Island, WA',
     'Taholah, WA',
     'Aberdeen, WA',
     'Raymond, WA',
     'Long Beach, WA',
     'Centralia, WA',
     'Longview, WA',
     'Elma, WA',
     'Pe Ell, WA',
     'Cathlamet, WA']
cluster2 = ['Seattle, WA',
     'Bellevue, WA',
     'Renton, WA',
     'Issaquah, WA',
     'North Bend, WA',
     'Tacoma, WA',
     'Bremerton, WA',
     'Union, WA',
     'Quilcene, WA',
     'Port Townsend, WA',
     'Sequim, WA',
     'Port Angeles, WA',
     'Vancouver, WA',
     'Winston, WA',
     'Yale Park, WA',
     'Glenwood, WA',
     'Maple Valley, WA',
     'Everett, WA',
     'Monroe, WA',
     'Gold Bar, WA',
     'Bellingham, WA',
     'Mount Vernon, WA',
     'Darrington, WA',
     'Concrete, WA',
     'Eatonville, WA',
     'Orting, WA']
cluster3 = ['Easton, WA',
     'Cle Elum, WA',
     'Liberty Lake, WA',
     'Scenic, WA',
     'Winthrop, WA',
     'Omak, WA',
     'Brewster, WA',
     'Leavenworth, WA',
     'Wenatchee, WA',
     'Moore, WA',
     'Rockford, WA',
     'Republic, WA',
     'Colville, WA',
     'Ione, WA',
     'Entiat, WA',
     'Ford, WA',
     'Keller, WA']
cluster4 = ['Quincy, WA',
     'George, WA',
     'Ritzville, WA',
     'Moses Lake, WA',
     'Richland, WA',
     'Kennewick, WA',
     'Odessa, WA',
     'Coulee City, WA',
     'LaCrosse, WA',
     'Connell, WA',
     'Sixprong, WA',
     'Dayton, WA',
     'Sunnyside, WA']
cluster5 = ['Ellensburg, WA',
     'Sprague, WA',
     'Cheney, WA',
     'Spokane, WA',
     'Packwood, WA',
     'Tire Junction, WA',
     'Goldendale, WA',
     'Kittitas, WA',
     'Yakima, WA',
     'Mansfield, WA',
     'Carson, WA',
     'Trout Lake, WA',
     'Parrott Crossing, WA',
     'Peaceful Valley, WA',
     'Walla Walla, WA',
     'Colfax, WA',
     'Wilbur, WA',
     'Pomeroy, WA',
     'Klickitat, WA',
     'Clarkston, WA']

clusters = [cluster1, cluster2, cluster3, cluster4, cluster5]
iconColors = ["green", "red", "blue", "darkpurple", "pink"]

usdmFileName = "usdm_current.json"
downloadUsdmDroughtSeverityGeoJson(usdmFileName)

cdmFilenames = ["CDM_2408_D0_LR.geojson",
                "CDM_2408_D1_LR.geojson",
                "CDM_2408_D2_LR.geojson",
                "CDM_2408_D3_LR.geojson"]

waCenter = (47.7511, -120.7401)
waMap = folium.Map(location = waCenter, zoom_start = 7, tiles="TopPlusOpen.Color")

makeBoundaryLayer("counties_wa.json", "WA Counties").add_to(waMap)
makeBoundaryLayer("us-states.json", "US States", show=False).add_to(waMap)

makeDroughtSeverityLayer(usdmFileName, "US Drought Severity").add_to(waMap)

canadaDroughtLayer = folium.FeatureGroup(name = "Canada Drought Severity").add_to(waMap)
for cdmFileName in cdmFilenames:
    makeDroughtSeverityLayer(cdmFileName, "Canada").add_to(canadaDroughtLayer)

makeKoppenClassificationLayer("climate-classification.json",
                              "Köppen-Geiger Climate Classification", show=False).add_to(waMap)

for clusterId, cluster in enumerate(clusters):
    makeClusterLayer(cluster, clusterId, iconColors[clusterId], "Cluster " + str(clusterId)).add_to(waMap)

folium.LayerControl().add_to(waMap)
waMap.save("wa-usstates-usdm-cdm-koppen.html")

