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

html = """
"<p>Oooo</p><img width="60" src="alaska.png">"
"""

popupHanscom = folium.Popup(html,
                            show=True,)

folium.Marker(
    location=hanscom,
    popup=popupHanscom,
    tooltip="Hi!",
    icon=folium.Icon(color="red", icon="plane")
).add_to(bostonMap)

bostonMap.save("popups.html")