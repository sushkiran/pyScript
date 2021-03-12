import folium
import pandas

# Using Pandas
data = pandas.read_csv("Volcanoes_USA.txt")
longitude = list(data["LON"])
latitude = list(data["LAT"])
elevation = list(data["ELEV"])


def get_color(arg_elevation):
    if arg_elevation < 1000:
        return "green"
    elif 1000 <= arg_elevation < 3000:
        return "orange"
    else:
        return "red"


# Create a MAP-BOX
map_box = folium.Map(location=[32.58, -99.09], zoom_start=5)

# Create VOLCANO Feature group
volcano_fg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(latitude, longitude, elevation):
    colored_icon = folium.Icon(color=get_color(el))
    volcano_fg.add_child(
        folium.Marker(location=[lt, ln], popup='{:d}m'.format(int(el)), icon=colored_icon)
    )

# Create POPULATION Feature group
population_fg = folium.FeatureGroup(name="Population")

population_fg.add_child(
    folium.GeoJson(
        data=open('world.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {
            'fillColor': 'green' if x['properties']['POP2005'] < 10000000
            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
            else 'red'
        }
    )
)

map_box.add_child(volcano_fg)
map_box.add_child(population_fg)
map_box.add_child(folium.LayerControl())

map_box.save("Volcano_population.html")
print(map_box)
