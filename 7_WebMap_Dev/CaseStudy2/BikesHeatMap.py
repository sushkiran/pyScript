import folium
from folium import plugins
import pandas as pd

print(folium.__version__)


divvyStations_q3 = pd.read_csv('Divvy_Stations_2016_Q3.csv')
divvyStations_q4 = pd.read_csv('Divvy_Stations_2016_Q4.csv')

# combine and keep the first instance of id
divvyStations = pd.concat([divvyStations_q3, divvyStations_q4], axis=0).drop_duplicates(subset=['id'])
print(divvyStations.head())

CHICAGO_COORD = [41.8781, -87.6298]

map_heat = folium.Map(CHICAGO_COORD,
               zoom_start=11)

# mark each station as a point
# Uncomment the code below and check

# for index, row in divvyStations.iterrows():
#     folium.CircleMarker([row['latitude'], row['longitude']],
#                         radius=15,
#                         popup=row['name'],
#                         fill_color="#3db7e4",  # divvy color
#                         ).add_to(map_heat)


stationArr = [[row['latitude'],row['longitude']] for index, row in divvyStations.iterrows()]

# plot heatmap
map_heat.add_child(plugins.HeatMap(stationArr, radius=15))
map_heat.save("BikeStationHeatMap.html")
print(map_heat)

