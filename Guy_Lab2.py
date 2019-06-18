#Maddie Guy
#GEOG682, Lab 2
#18 June 2019

#This code uses QGIS to analyze to shapefiles (crime locations in DC in 2017, and police districts) to find out which district had
#the most crime in 2017, and how many incidents there were.

import processing #Import QGIS processing tools
districts = "S:/682/Summer19/mguy1/Police_Districts.shp" #Save police districts shapefile as new variable "districts"
crime = "S:/682/Summer19/mguy1/Crime_Incidents_in_2017.shp" #Save crime incidents shapefile as new variable "crime"

iface.addVectorLayer(districts,"districts","ogr") #Add districts crime shapefile to map
iface.addVectorLayer(crime,"crime","ogr") #Add crime shapefile to map

#Runs the processing tool "Join Attributes by Location" based on inputs specified in the second line. In this case, the districts
#are the "target" layer and the crime locations are the "join" layer.
processing.runalg("qgis:joinattributesbylocation",
    {'TARGET':districts,'JOIN':crime,'PREDICATE':u'contains','SUMMARY':1,'KEEP':1,'OUTPUT':"S:/682/Summer19/mguy1/dc_crime_join.shp"})

#Adds new join polygon to the map
dc_join = "S:/682/Summer19/mguy1/dc_crime_join.shp"
iface.addVectorLayer(dc_join, "join", "ogr")

#In 2017, the district with the most crimes was the Third District, with a total of 5,964 out of 33,082 crimes occuring within
#its boundaries.