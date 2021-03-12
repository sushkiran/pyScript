"""
Business challenge/requirement
SFO Police has shared crime data for year 2016. Data contains various incidents which have happened throughout
the year, along with the geolocation of the crime. You need to prepare effective web-maps to analyze and present
the data. SFO Commissioner of Police will reassign the forces based on the density of various crime.

Approach to Solve
1.  Display first 100 records from the data and play with parameters - tiles, zoom_start etc.
    Map will be saved in BasicWebMap.html – view it in browser
2.  For latest 7 days of data create WebMap of Crimes which are categorized as ROBBERY
3.  For latest 15 days of data create One WebMap of Crimes which are categorized as FRAUD and GAMBLING.
4.  For latest 7 days of data create WebMap of Crimes which are categorized as BURGLARY
"""
import folium
import pandas as pd

# common data
data = pd.read_csv('Police_Department_Incidents_Year_2016_.csv')
unique_dates = data['Date'].drop_duplicates().sort_values(ascending=False)
SAN_FRANCISCO = [37.77986, -122.42905]


# common functions
def get_zip_lists(condition, grp_name):
    if grp_name == 'Basic':
        return zip(
                list(data['X'][0:100]),
                list(data['Y'][0:100]),
                list(data['Address'][0:100])
        )
    else:
        return zip(
                list(data['X'][condition]),
                list(data['Y'][condition]),
                list(data['Address'][condition])
        )


def get_feature_group(condition, grp_name, color):
    feature_grp = folium.FeatureGroup(name=grp_name)

    for longitude, latitude, address in get_zip_lists(condition, grp_name):
        colored_icon = folium.Icon(color=color)
        feature_grp.add_child(
            folium.Marker(location=[latitude, longitude], popup=address.title(), icon=colored_icon)
        )

    return feature_grp


# Create the map object for the container
map_object = folium.Map(location=SAN_FRANCISCO, zoom_start=13)


# 1. Create Basic Feature group
fg_top_100 = get_feature_group(None, 'Basic', 'blue')
map_object.add_child(fg_top_100)


# 2. Create Robbery Feature group
last7D_robbery = (data['Category'] == 'ROBBERY') & (data['Date'].isin(unique_dates[:7]))
fg_robbery = get_feature_group(last7D_robbery, 'Robbery', 'red')
map_object.add_child(fg_robbery)


# 3. Create Fraud/Gambling Feature group
last15D_fraud = (data['Category'].isin(['FRAUD', 'GAMBLING'])) & (data['Date'].isin(unique_dates[:15]))
fg_fraud_gambling = get_feature_group(last15D_fraud, 'Fraud & Gambling', 'green')
map_object.add_child(fg_fraud_gambling)


# 4. Create Burglary Feature group
last7D_burglary = (data['Category'] == 'BURGLARY') & (data['Date'].isin(unique_dates[:7]))
fg_burglary = get_feature_group(last7D_burglary, 'Fraud & Gambling', 'purple')
map_object.add_child(fg_burglary)


# Final addition & save as HTML
map_object.add_child(folium.LayerControl())
map_object.save("BasicWebMap.html")
print('Done')
