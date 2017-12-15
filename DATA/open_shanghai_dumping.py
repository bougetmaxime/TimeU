
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
    and service_score > 7
    and review_count > 2000
    and (c.parent = '美食'
    or  c.category = '美食')
    
'''

food_place = pd.read_sql(query, conn)


# In[37]:


#print(food_place.describe())

Nbr_food_around_U=food_place.name.count()
print('Number of Restaurant around you ')
print(Nbr_food_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:





#plt.figure(figsize=(8,6))
#plt.scatter( food_place.latitude, food_place.longitude)
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

cinema_place = pd.read_sql(query, conn)


# In[37]:

#print(cinema_place.describe())

Nbr_cine_around_U=cinema_place.name.count()
print('Number of cinema around you ')
print(Nbr_cine_around_U)


# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( cinema_place.latitude, cinema_place.longitude)
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
    and avg_rating > 40      
    and review_count > 100    
    and (c.parent = '购物'
    or  c.category = '购物')
    
'''

shop_place = pd.read_sql(query, conn)


# In[37]:
print(shop_place.describe())

Nbr_shop_around_U=shop_place.name.count()
print('Number of Shop around you ')
print(Nbr_shop_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( shop_place.latitude, shop_place.longitude)
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

artculture_place = pd.read_sql(query, conn)


# In[37]:
#print(artculture_place.describe())

Nbr_art_culture_around_U=artculture_place.name.count()
print('Number of Art & culture place around you ')
print(Nbr_art_culture_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( artculture_place.latitude, artculture_place.longitude)
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

escapegame_place = pd.read_sql(query, conn)


# In[37]:
#print(escapegame_place.describe())

Nbr_escape_game_around_U=escapegame_place.name.count()
print('Number of Escape game place around you ')
print(Nbr_escape_game_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( escapegame_place.latitude, escapegame_place.longitude)
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

game_place = pd.read_sql(query, conn)


# In[37]:
#print(game_place.describe())

Nbr_game_center_around_U=game_place.name.count()
print('Number of Game center around you ')
print(Nbr_game_center_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')

# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( game_place.latitude, game_place.longitude)
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

swimming_place = pd.read_sql(query, conn)


# In[37]:

#print(swimming_place.describe())

Nbr_swimming_pool_around_U=swimming_place.name.count()
print('Number of Swimming pool around you ')
print(Nbr_swimming_pool_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')

# In[42]:

#plt.figure(figsize=(8,6))
#plt.scatter( swimming_place.latitude, swimming_place.longitude)
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

gym_place = pd.read_sql(query, conn)


# In[37]:


#print(gym_place.describe())

Nbr_gym_around_U=gym_place.name.count()
print('Number of Gym around you ')
print(Nbr_gym_around_U)

# In[40]:


color = sns.color_palette()
plt.style.use('ggplot')


# In[42]:





#plt.figure(figsize=(8,6))
#plt.scatter( gym_place.latitude, gym_place.longitude)
#plt.xlim( 31.177, 31.207 )
#plt.ylim( 121.41, 121.441 ) 
#plt.title('GYM AROUND ME')
#plt.ylabel('longitude', fontsize=12)
#plt.xlabel('latitude', fontsize=12)
#plt.show()

















# In[52]:


df = pd.read_csv('C:\\Users\\DELL\\Desktop\\Urban Data Hackathon\\UTSEUS-MOBIKE-shanghai_full.csv')


# In[53]:


query = '''
SELECT business_id, group_concat(tag, ' ')as tags
FROM venues_tags
group by business_id
'''
df = pd.read_sql(query, conn)


# In[54]:


sentences = []
for tags in df.tags.values:
    if len(tags.split(' ')) > 1:
        sentences.append(tags.split(' '))


# In[55]:


print (len(sentences))


# In[58]:


#login import
from gensim.models import word2vec

#set values for various parameters
num_features = 500 #word vector dimensionality
min_word_count = 10 #minimum word count
num_workers = 4 #number of threads to run in parallel
context = 3 #context windows
downsampling = 1e-3

model = word2vec.Word2Vec(sentences, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
model_name = "500features_10minwords_3context_dianping"
model.save(model_name)


# In[60]:



G = nx.Graph()
for tag in model.wv.vocab.keys():
    G.add_node(tag)
    for word, similarity in model.most_similar(tag):
        G.add_node(word)
        G.add_edge(tag, word, weight=similarity)
nx.write_gexf(G, 'tags-similarity.gexf')
        


# In[61]:


model.most_similar('PIZZA')


# In[62]:


for word, similarity in model.most_similar('PIZZA'):
    print (word, similarity)

