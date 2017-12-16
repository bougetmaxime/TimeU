
# coding: utf-8
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

#get_ipython().magic(u'matplotlib inline')



conn = sqlite3.connect('/Users/maximebouget/Documents/Entrepreneurial/Hackathon/Urban Data-Shanghai-14:12:17/data/UTSEUS-shanghai-dianping.db')

####################### Food 美食  around you :

query = ''' 
SELECT c.category, name, longitude, latitude, avg_price, photo_count, address, service_score, review_count, avg_rating
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_price > 0
    and avg_rating > 30
    and service_score > 6.5
    and review_count > 1000
    and (c.parent = '美食'
    or  c.category = '美食')
    
'''


food_places = pd.read_sql(query, conn)






# In[37]:


#print(food_places.describe())

'''Nbr_food_around_U=food_places.name.count()
print('Number of Restaurant around you ')
print(Nbr_food_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:





#plt.figure(figsize=(8,6))
#plt.scatter( food_places.latitude, food_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('FOOD AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()




################## Cinéma 电影院   around you :

query = ''' 
SELECT c.category, name, longitude, latitude, avg_price, photo_count, address, service_score, review_count, avg_rating
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_price > 0
    and service_score > 5
    and review_count > 100
    and (c.parent = '电影院'
    or  c.category = '电影院')
    
'''

cinema_places = pd.read_sql(query, conn)


# In[37]:

#print(cinema_places.describe())

'''Nbr_cine_around_U=cinema_places.name.count()
print('Number of cinema around you ')
print(Nbr_cine_around_U)'''


# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( cinema_places.latitude, cinema_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('CINEMA AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()



################## Shop 购物   around you :

query = ''' 
SELECT c.category, name, longitude, latitude, photo_count, address, service_score, review_count, avg_rating 
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and service_score > 7    
    and avg_rating > 35     
    and review_count > 125    
    and (c.parent = '购物'
    or  c.category = '购物')
    
'''

shop_places = pd.read_sql(query, conn)


# In[37]:
#print(shop_places.describe())

'''Nbr_shop_around_U=shop_places.name.count()
print('Number of Shop around you ')
print(Nbr_shop_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( shop_places.latitude, shop_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('SHOP AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()



################## Art and Culture   文化艺术 around you :

query = ''' 
SELECT c.category, name, longitude, latitude, photo_count, address, review_count, avg_rating 
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_rating > 35   
    and review_count > 100   
    and (c.parent = '文化艺术'
    or  c.category = '文化艺术')
    
'''

artculture_places = pd.read_sql(query, conn)


# In[37]:
#print(artculture_places.describe())

'''Nbr_art_culture_around_U=artculture_places.name.count()
print('Number of Art & culture place around you ')
print(Nbr_art_culture_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( artculture_places.latitude, artculture_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('Art & Culture AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()




################## Escape game 密室  around you :

query = ''' 
SELECT c.category, name, longitude, latitude, avg_price, photo_count, address, review_count, avg_rating
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_rating > 40  
    and review_count > 100 
    and (c.parent = '密室'
    or  c.category = '密室')
    
'''

escapegame_places = pd.read_sql(query, conn)


# In[37]:
#print(escapegame_places.describe())

'''Nbr_escape_game_around_U=escapegame_places.name.count()
print('Number of Escape game place around you ')
print(Nbr_escape_game_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( escapegame_places.latitude, escapegame_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('Escape Game AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()






################## Game place 桌球馆   (pool, vidéo game, ...) around you :

query = ''' 
SELECT c.category, name, longitude, latitude, avg_price, photo_count, address, review_count, avg_rating
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_rating > 30    
    and review_count > 100   
    and (c.parent = '桌球馆'
    or  c.category = '桌球馆')
    
'''

game_places = pd.read_sql(query, conn)


# In[37]:
#print(game_places.describe())

'''Nbr_game_center_around_U=game_places.name.count()
print('Number of Game center around you ')
print(Nbr_game_center_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')

# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( game_places.latitude, game_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('Game center AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()


################## Swimming pool 游泳馆 around you :

query = ''' 
SELECT c.category, name, longitude, latitude, photo_count, address, review_count, avg_rating
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_rating > 30 
    and review_count > 10  
    and (c.parent = '游泳馆'
    or  c.category = '游泳馆')
    
'''

swimming_places = pd.read_sql(query, conn)


# In[37]:

print(swimming_places)

'''Nbr_swimming_pool_around_U=swimming_places.name.count()
print('Number of Swimming pool around you ')
print(Nbr_swimming_pool_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')

# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( swimming_places.latitude, swimming_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('Swimming pool AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()




####################### GYM 健身中心  around you :

query = ''' 
SELECT c.category, name, longitude, latitude, avg_price, photo_count, address, review_count, avg_rating
from venues v 
join venue_categories vc on (v.business_id = vc.business_id) 
    join categories c on (vc.category = c.category) 
where 
        latitude < 31.191472 + 0.015
    and latitude > 31.191472 - 0.015
    and longitude < 121.426425  + 0.015
    and longitude > 121.426425  - 0.015
    and avg_price > 0
    and avg_rating > 35      
    and review_count > 100  
    and (c.parent = '健身中心'
    or  c.category = '健身中心')
    
'''

gym_places = pd.read_sql(query, conn)


# In[37]:


#print(gym_places.describe())

'''Nbr_gym_around_U=gym_places.name.count()
print('Number of Gym around you ')
print(Nbr_gym_around_U)'''

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:





#plt.figure(figsize=(8,6))
#plt.scatter( gym_places.latitude, gym_places.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('GYM AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()
















