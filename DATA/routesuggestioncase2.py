consumer_lat = 31.191472
consumer_long= 121.426425 
position_square= 0.015

# Import:
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import logging
import networkx as nx
import csv
import math
import geojson
from geojson import Point, LineString, Feature, FeatureCollection






####### SUGESTION OF TRACK

# Start point

my_starting_point = (consumer_lat,consumer_long)

# Function Distance
def get_distance(pos1,pos2) :
    dst = math.pow((pos1[0]-pos2[0]),2)+math.pow((pos1[1]-pos2[1]),2)
    return dst



 
########## Case 2 = Museum  ----> Swimming pool

#1° Art & Culture :
artculture_spamreader = csv.reader(open('/Users/maximebouget/Documents/Entrepreneurial/Hackathon/Urban Data-Shanghai-14:12:17/Github_TimeU/DATA/artculture_places.csv','r'),delimiter='|')

closest_artculture = (None, None)
for artculture_place in artculture_spamreader:
    lon = float(artculture_place[2])
    lat = float(artculture_place[3])
    point = (lon, lat)
    distance= get_distance(my_starting_point,point)
    if closest_artculture[0] is None:
        closest_artculture = (artculture_place, distance)
    elif closest_artculture[1] > distance:
        closest_artculture = (artculture_place, distance)

print(closest_artculture)

#2° Swimming pool:
swim_spamreader = csv.reader(open('/Users/maximebouget/Documents/Entrepreneurial/Hackathon/Urban Data-Shanghai-14:12:17/Github_TimeU/DATA/swim_places.csv','r'),delimiter='|')
my_artculture_point =(float(closest_artculture[0][3]),float(closest_artculture[0][2]))
closest_swim = (None, None)
for swim_place in swim_spamreader:
    lon = float(swim_place[2])
    lat = float(swim_place[3])
    point = (lon, lat)
    distance= get_distance(my_artculture_point,point)
    if closest_swim[0] is None:
        closest_swim = (swim_place, distance)
    elif closest_swim[1] > distance:
        closest_swim = (swim_place, distance)

print(closest_swim)


caseTwoartculture=(closest_artculture[0][0],closest_artculture[0][1],closest_artculture[0][2],closest_artculture[0][3],closest_artculture[0][5],'None')
caseTwoswim=(closest_swim[0][0],closest_swim[0][1],closest_swim[0][2],closest_swim[0][3],closest_swim[0][8])
caseTwo= (caseTwoartculture, caseTwoswim)
print(caseTwo)


#Transforme to GEOJSON file

'''featureCollection=[]
for case in caseTwo:
    place = Point((float(caseTwo[i][3]),float(caseTwo[i][2])))
    name = caseTwo[i][1]
    adress = caseTwo[i][4]
    grade = caseTwo[i][5]
    feature=Feature(geometry=place, properties={'Name':name,'Adress':adress,'Grade':grade})
    featureCollection.append(feature)
featureCollection=FeatureCollection(featureCollection)
dump=geojson.dumps(featureCollectionline,sort_keys=True)
print(dump)'''


featureCollection=[]
for i in range(0,len(caseTwo)-2):
    start = Point((float(caseTwo[i][3]),float(caseTwo[i][2])))
    end = Point((float(caseTwo[i+1][3]),float(caseTwo[i+1][2])))
    linestring = LineString([start, end])
    print(linestring)
    name = caseTwo[i][0] + '-->' + caseTwo[i+1][0]
    feature=Feature(geometry=linestring, properties={'Name':name})
    featureCollection.append(feature)
featureCollection=FeatureCollection(featureCollection)

dump=geojson.dumps(featureCollection,sort_keys=True)
print(dump)
