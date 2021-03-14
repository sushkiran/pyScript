"""
ANALYSIS using DATA WRANGLING
1. What are the top 10 Zipcodes for 911?
2. Are Zipcodes 19446 and 19090 present?
3. What are the top 4 townships (twp) for 911 calls?
4. Which of the following township are not present?-- LOWER POTTSGROVE, NORRISTOWN, HORSHAM, ABINGTON
5. What is the most common Reason for a 911 call based on Reason Column? Which comes second?.
6. Which day got maximum calls for EMS and how many?
7. On which day traffic calls were lowest?
8. Which month saw highest calls for fire?
9. Which areas haves the lowest traffic calls?

ANALYSIS using DATA VISUALIZATION:
1. Plot barchart using mat plot for 911 calls by Reason.
2. How can you plot the bars horizontally ?
3. Create a count-plot of the Day of Week column with the hue based of the Reason column
4. Create a count-plot month wise
5. Create Web Map for Sunday Traffic Calls.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import folium

'''
------------------------------
ANALYSIS using DATA WRANGLING
------------------------------
'''

data = pd.read_csv('911.csv')
data['reason'] = data.title.str.split(':').str[0]
data['day'] = pd.to_datetime(data['timeStamp']).dt.strftime('%A')
data['month'] = pd.to_datetime(data['timeStamp']).dt.strftime('%B')

top_10_zipcodes = data.zip.value_counts().head(10).index.astype(int).tolist()
print('1. Top 10 Zipcodes for 911 are', top_10_zipcodes)

zip_check = all(elem in top_10_zipcodes for elem in [19090, 19446])
print('2. The Zipcodes 19446 & 19090 {} a part of top 10 zipcodes'.format('"ARE"' if zip_check else '"ARE NOT"'))

top_4_towns = data.twp.value_counts().head(4).index.tolist()
print('3. Top 4 Townships for 911 calls are', top_4_towns)

missing_towns = [elem for elem in ['LOWER POTTSGROVE', 'NORRISTOWN', 'HORSHAM', 'ABINGTON'] if elem not in top_4_towns]
print('4. The Townships {} are not in the top 4 townships for 911 calls.'.format(missing_towns))

top_2_reasons = data.reason.value_counts().head(2).index.tolist()
print('5. Top 2 Reasons for 911 calls are', top_2_reasons)

ems = data[data.reason == 'EMS'].groupby('day').count().sort_values(by='e', ascending=False).head(1)
print('6. A {} receives the highest EMS calls, with a count of {}.'.format(ems.index[0], ems.e[0]))

traffic = data[data.reason == 'Traffic'].groupby('day').count().sort_values(by='e').head(1)
print('7. A {} receives the lowest Traffic calls, with a count of {}.'.format(traffic.index[0], traffic.e[0]))

fire = data[data.reason == 'Fire'].groupby('month').count().sort_values(by='e', ascending=False).head(1)
print('8. The month of {} saw the highest Fire calls, with a count of {}.'.format(fire.index[0], fire.e[0]))

area = data[data.reason == 'Traffic'].groupby('twp').count().sort_values(by='e').head(1)
print('9. Township(s) with lowest Traffic calls is(are) {}, with a count of {}.'.format(area.index[0], area.e[0]))

'''
-------------------------------------------
ANALYSIS using DATA VISUALIZATION - CHARTS
-------------------------------------------
'''

fig, ax = plt.subplots(2, 2)
fig.tight_layout(h_pad=2)

calls_by_reason = data.groupby('reason').agg('count')
calls_by_reason.reset_index(inplace=True)

plt.subplot(2, 2, 1)
plt.bar(calls_by_reason['reason'], calls_by_reason['e'])
plt.title('V-Bar chart by Reason')

plt.subplot(2, 2, 2)
plt.barh(calls_by_reason['reason'], calls_by_reason['e'])
plt.title('H-Bar chart by Reason')

plt.subplot(2, 2, 3)
sns.countplot(
    x="day", hue="reason", data=data[['day', 'reason']],
    order=[calendar.day_name[x] for x in range(0, 7)]
)
plt.title('Count plot Day-Reason')
plt.xticks(rotation=45, ha='right')
plt.xlabel(None)

plt.subplot(2, 2, 4)
sns.countplot(
    hue="variable", x="value", data=pd.melt(data[['month']]),
    order=[calendar.month_name[x] for x in range(1, 13)]
)
plt.title('Count plot Month-wise')
plt.xticks(rotation=45, ha='right')
plt.xlabel(None)

plt.get_current_fig_manager().window.state('zoomed')
plt.subplots_adjust(top=0.90, bottom=0.1, left=0.08)
plt.suptitle('Montgomery Visuals')

plt.show()
plt.close()

'''
--------------------------------------------
DATA VISUALIZATION - WEB MAP (TRAFFIC CALLS)
--------------------------------------------
'''

MONTGOMERY = [40.13, -75.22]

sunday_traffic = data.query("reason=='Traffic' & day=='Sunday'")[['lat', 'lng', 'twp']].value_counts()
feature_grp = folium.FeatureGroup(name='Sunday Traffic Calls')

for index, value in sunday_traffic.items():
    color = 'green' if value in range(10) else ('orange' if value in range(10, 100) else 'red')
    popup_text = '{} ({}) call' if value == 1 else '{} ({}) calls'
    feature_grp.add_child(
        folium.Marker(
            location=[index[0], index[1]], popup=popup_text.format(index[2].title(), value),
            icon=folium.Icon(color=color)
        )
    )

map_object = folium.Map(location=MONTGOMERY, zoom_start=12)
map_object.add_child(feature_grp)
map_object.add_child(folium.LayerControl())
map_object.save("traffic.html")

print('Done')
