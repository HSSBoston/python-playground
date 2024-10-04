import folium, folium.plugins, csv
import datetime 

nyCenter = (40.7128, -74.0060)
usMap = folium.Map(location = nyCenter, zoom_start = 8)


data = [
   [[40.7128,-74.0060,0.3]],
   [[40.7128,-74.0060,0.5]],
   [[40.7128,-74.0060,0.8]],
   [[40.7128,-74.0060,0.95]]
]

#表示する時刻（サンプルデータのデータ数と一致している必要あり）
time_index = [
   datetime.time(20, 31, 0, 0).strftime("%H:%M:%S"),
   datetime.time(20, 38, 0, 0).strftime("%H:%M:%S"),
   datetime.time(20, 40, 0, 0).strftime("%H:%M:%S"),
   datetime.time(21, 26, 0, 0).strftime("%H:%M:%S")
]


folium.plugins.HeatMapWithTime( #ヒートマップを作成
      data,
      index=time_index, #時刻指定
      auto_play=True,
      radius=30, #ヒートマップの大きさ
      max_opacity=0.3,
#       gradient={0.1: 'blue', 0.25: 'lime', 0.5:'yellow',0.75: 'orange', 0.9:'red'}#色度合い指定
).add_to(usMap)


usMap.save("heatmap-withtime.html")
