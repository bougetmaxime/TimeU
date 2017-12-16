
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
    
