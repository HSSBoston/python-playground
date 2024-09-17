import folium
from folium.plugins import HeatMap

m = folium.Map(location=[35.6895, 139.6917], zoom_start=12)

data = [[35.6895, 139.6917, 0.5], [35.6896, 139.6918, 0.8], [35.6897, 139.6919, 0.3]]

HeatMap(data).add_to(m)
m.save("heatmap.html")