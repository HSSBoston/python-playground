# https://leaflet-extras.github.io/leaflet-providers/preview/
# USGS.USTopo
# OpenTopoMap
# TopPlusOpen.Color
# Stadia.StamenTerrainBackground
# Thunderforest.Landscape
# Jawg.Terrain
# Esri.WorldStreetMap
# Esri.WorldPhysical
# NASAGIBS.ViirsEarthAtNight2012
#
# https://fontawesome.com/

import folium

logan = (42.365792221496, -71.00966724673485)
hanscom = (42.46495591784104, -71.2869683230597)

bostonMap = folium.Map(location=logan, zoom_start=11)

folium.Marker(
    location=logan,
    popup="<b><i>Logan Airport</i><b>",
    tooltip="Click me!",
    icon=folium.Icon(color="green", icon="cloud")
).add_to(bostonMap)

folium.Marker(
    location=hanscom,
    popup="<b><i>Hanscom Airport</i><b>",
    tooltip="Hi!",
    icon=folium.Icon(color="red", icon="plane")
).add_to(bostonMap)

folium.CircleMarker(
    location=(42.36092708954118, -71.06230482413301),
    radius=40, # meters
    color='#ff0000',
    fill_color='#0000ff'
    #popup=
).add_to(bostonMap)

bostonMap.add_child(folium.LatLngPopup())
bostonMap.save("logan.html")



northBend = (47.495572913837606, -121.78408248964297)


northBendMap = folium.Map(location=northBend, zoom_start=10,
                          tiles="OpenTopoMap")
folium.Marker(
    location=northBend,
    popup="<b><i>North Bend, WA</i><b>",
    tooltip="Click me!",
    icon=folium.Icon(icon="fire")
).add_to(northBendMap)
northBendMap.save("north-bend.html")

