import pandas as pd 
import numpy as np 
import warnings

hotels=pd.read_csv('zomato.csv')
#print(hotels.head())

#TASK 1
#Removing unwanted columns 

hotels.drop("address",axis=1,inplace=True)
hotels.drop("phone",axis=1,inplace=True)
#print(hotels.head())


#renaming columns
# number=len('name')
# hotels.insert(loc=0,column='id',value=number,allow_duplicates=False)

#TASK 2 
#hotels.insert(0, 'Id', range(0, 0 + len(hotels)))
hotels.rename(columns={'rate':'rating','listed_in(type)':'type','approx_cost(for two people)':'approx_cost'},inplace=True)

print(hotels.columns)
# print(hotels.head())

hotels.isnull().sum()

#TASK 3
hotels.dropna(subset=['name'],inplace=True)

hotels['online_order'].fillna(value='Na',inplace=True)

    #handling null values of book_table
hotels['book_table'].fillna(value='NA',inplace=True)
    #handling null values of rating
hotels['rating'].fillna(value=0,inplace=True)
    #handling null values of votes
hotels['votes'].fillna(value=0,inplace=True)
    #handling null values of location
hotels['location'].fillna(value='NA',inplace=True)
    #handling null values of rest_type
hotels['rest_type'].fillna(value='NA',inplace=True)
    #handling null values of dishliked
hotels['dish_liked'].fillna(value='NA',inplace=True)
    #handling null values of cuisines
hotels['cuisines'].fillna(value='NA',inplace=True)
    #handling null values of approxcost
hotels['approx_cost'].fillna(value=0,inplace=True)
    #handling null values of type
hotels['type'].fillna(value='NA',inplace=True)


hotels.isnull().sum()

#TASK 4 

hotels.drop_duplicates(subset=['name','online_order','book_table','rating','votes','location','rest_type','dish_liked','cuisines','approx_cost','type'],keep='first',inplace=True)
#df.drop_duplicates(subset=['name','online_order'],keep='first',inplace=True)
print(hotels.shape)

#removing irrelevant text from all the columns

#TASK 5

hotels=hotels[hotels['name'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['online_order'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['book_table'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['rating'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['votes'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['location'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['rest_type'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['dish_liked'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['cuisines'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['approx_cost'].str.contains('RATED|Rated')==False]
hotels=hotels[hotels['type'].str.contains('RATED|Rated')==False]


#check for unique values in each column and handle the irrelevant values

#TASK 6
hotels=hotels[hotels['online_order'].str.contains('Yes|No')==True]
hotels['rating']=hotels['rating'].apply(lambda x:x.replace('/5',""))
hotels['rating']=hotels['rating'].replace(['NEW','-'],0)
print(hotels.head(11))

#TASK 7

dataframe['name']=dataframe['name'].replace({'[Ãx][^A-Za-z]+': ''}, regex=True)


#MODULE 2 


#TASK 1 
SELECT name,votes,rating
FROM zomato
WHERE type = 'Delivery'
ORDER BY votes DESC
LIMIT 5;


#TASK 2
 
select name,rating,location,type
from zomato
where type ='Delivery' and location ='Banashankari'
order by rating desc
limit 5;

# TASK 3 
select(select rating from zomato where location = 'indiranagar" order by approx_cost asc limit 1) as rating1 ,
    (select rating from  zomato where location ="indiranagar" order by approx_cost desc limit1) as rating2;
    

#  Task 4
select sum(votes),online_order from zomato group by online_order

# TASK 5 


select type,count(type) as Number_Of_Restaurants,sum(votes) as Total_Votes,AVG(rating) as Avg_Rating
from zomato where type != "NA"
group by type order by Total_Votes desc;

#TASK 6

SELECT name, dish_liked, rating, votes
FROM zomato
WHERE rating = (SELECT MAX(rating) FROM zomato)
AND online_order = 'Yes'
ORDER BY votes DESC
LIMIT 1;

# TASK 7

select name,rating,votes,online_order 
from zomato 
where rating>3 and votes>150 and online_order="No" 
order by votes desc limit 15;

