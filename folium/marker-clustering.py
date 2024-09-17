import folium
from folium.plugins import MarkerCluster

m = folium.Map(location=[35.6895, 139.6917], zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)

for i in range(100):
    folium.Marker(location=[35.6895 + i*0.001, 139.6917 + i*0.001]).add_to(marker_cluster)

m.save("marker_clustering.html")