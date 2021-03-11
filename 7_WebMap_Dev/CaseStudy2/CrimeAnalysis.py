"""
Business challenge/requirement
You are a data analyst in SanFrancisco(SFO) City IT Department. SFO Police has shared crime data for year 2016.
Data contains various incidents which have happened throughout the year, along with the geolocation of the crime.
You need to prepare effective web-maps to analyze and present the data. SFO Commissioner of Police will reassign
the forces based on the density of various crime

Key issues
Data should be displayed pictorially in map to get the desired attention of top authorities.

Data volume
Approx 150K records – file Police_Department_Incidents_Year_2016_.csv
(Data is downloaded from https://datasf.org/opendata/)

Business benefits
SFO City Corporation is looking to reduce crime rate based on effective relocation of police personnel,
thus reducing overall security cost.

Approach to Solve
You have to use fundamentals of WebMap covered in module 7 and create following 4 maps.
1.  Display first 100 records from the data and play with parameters - tiles, zoom_start etc.
    Map will be saved in BasicWebMap.html – view it in browser
2.  For latest 7 days of data create WebMap of Crimes which are categorized as ROBBERY
3.  For latest 15 days of data create One WebMap of Crimes which are categorized as FRAUD and GAMBLING.
    Change the icon to font awesome icon (http://fontawesome.io/icons/)
4.  BONUS ASSIGNMENT -- Display heatmap for Divvy Bikes.
    Divvy Bikes runs bike rental service in Chicago and their bike station geolocation data is shared.
    Refer to BikesHeatMap.py and Divvy_Stations_2016_Q3.csv, Divvy_Stations_2016_Q4.csv

Enhancements for code
1.  Lot of visual options are available to change the map.
    You can refer to https://python-visualization.github.io/folium/modules.html for options
2.  Change the code to create web-map for 'BURGLARY ' for last 7 days
3.  BONUS ASSIGNMENT – Uncomment the code see the changes

"""