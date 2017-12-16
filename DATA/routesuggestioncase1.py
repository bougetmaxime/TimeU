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



 
########## Case 1 = Buy T-shirt   + Food  ----> Cinéma 

#1° Shop :
shop_spamreader = csv.reader(open('/Users/maximebouget/Documents/Entrepreneurial/Hackathon/Urban Data-Shanghai-14:12:17/Github_TimeU/DATA/shop_places.csv','r'),delimiter='|')

closest_shop = (None, None)
for shop_place in shop_spamreader:
    lon = float(shop_place[2])
    lat = float(shop_place[3])
    point = (lon, lat)
    distance= get_distance(my_starting_point,point)
    if closest_shop[0] is None:
        closest_shop = (shop_place, distance)
    elif closest_shop[1] > distance:
        closest_shop = (shop_place, distance)

print(closest_shop)

#2° Food:
food_spamreader = csv.reader(open('/Users/maximebouget/Documents/Entrepreneurial/Hackathon/Urban Data-Shanghai-14:12:17/Github_TimeU/DATA/food_places.csv','r'),delimiter='|')
my_shop_point =(float(closest_shop[0][3]),float(closest_shop[0][2]))
closest_food = (None, None)
for food_place in food_spamreader:
    lon = float(food_place[2])
    lat = float(food_place[3])
    point = (lon, lat)
    distance= get_distance(my_shop_point,point)
    if closest_food[0] is None:
        closest_food = (food_place, distance)
    elif closest_food[1] > distance:
        closest_food = (food_place, distance)

print(closest_food)

#3° Cinema:
cinema_spamreader = csv.reader(open('/Users/maximebouget/Documents/Entrepreneurial/Hackathon/Urban Data-Shanghai-14:12:17/Github_TimeU/DATA/cinema_places.csv','r'),delimiter='|')
my_food_point =(float(closest_food[0][3]),float(closest_food[0][2]))
closest_cinema = (None, None)
for cinema_place in cinema_spamreader:
    lon = float(cinema_place[2])
    lat = float(cinema_place[3])
    point = (lon, lat)
    distance= get_distance(my_food_point,point)
    if closest_cinema[0] is None:
        closest_cinema = (cinema_place, distance)
    elif closest_cinema[1] > distance:
        closest_cinema = (cinema_place, distance)

print(closest_cinema)

caseOneshop=(closest_shop[0][0],closest_shop[0][1],closest_shop[0][2],closest_shop[0][3],closest_shop[0][5],closest_shop[0][6])
caseOnefood=(closest_food[0][0],closest_food[0][1],closest_food[0][2],closest_food[0][3],closest_food[0][6],closest_food[0][7])
caseOnecinema=(closest_cinema[0][0],closest_cinema[0][1],closest_cinema[0][2],closest_cinema[0][3],closest_cinema[0][6],closest_cinema[0][7])
caseOne= (caseOneshop, caseOnefood, caseOnecinema)
print(caseOne)


#Transforme to GEOJSON file

featureCollection=[]
for case in caseOne:
    place = Point((float(case[3]),float(case[2])))
    name = case[1]
    adress = case[4]
    grade = case[5]
    feature=Feature(geometry=place, properties={'Name':name,'Adress':adress,'Grade':grade})
    featureCollection.append(feature)
featureCollection=FeatureCollection(featureCollection)
dump=geojson.dumps(featureCollection,sort_keys=True)
print(dump)

'''
featureCollection=[]
for i in range(0,len(caseOne)-2):
    start = Point((float(caseOne[i][3]),float(caseOne[i][2])))
    end = Point((float(caseOne[i+1][3]),float(caseOne[i+1][2])))
    linestring = LineString([start, end])
    print(linestring)
    name = caseOne[i][1]
    feature=Feature(geometry=linestring, properties={'Name':name})
    featureCollection.append(feature)
featureCollection=FeatureCollection(featureCollection)

dump=geojson.dumps(featureCollection,sort_keys=True)
print(dump)'''

