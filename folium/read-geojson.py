import folium

m = folium.Map([43, -100], zoom_start=4)

url = "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"

folium.GeoJson(url).add_to(m)

m.save("geojson.html")