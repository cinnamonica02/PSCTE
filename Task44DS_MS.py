#!/usr/bin/env python
# coding: utf-8

# # MySQL MongoDB 🍓

# In[35]:


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://cinnamonica02:dodos@cluster0.1tcx1p8.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

import pymongo
from pymongo import MongoClient

# client = pymongo.MongoClient('mongodb+srv://cinnamonica02:<clowy>@cluster0.p14k0rn.mongodb.net/')

# Creating our Database

db = client['aca']

# Creating our Collectionn

coll_create = db['dl_details']

# Inserting data on our collection using dict

data = {'name': 'agucate con arroz',
        'class': 'perfect',
        'timing': 'eternity'
}

coll_create.insert_one(data) # wouldve worked but its not
                             # running bc I failed to auth
                             # my acc :c 

data1 = {'email_id': 'agca@gmail.com ',
         'phone_num': 19347857382,
}

coll_create.insert_one(data1)

#data2 = {
#   'qualities': ['fantastic', 'awesome', 'fabulous'],
#    'preptime': ['quick' , 'and', 'easy']
#}

#coll_create.insert_one('data2')

# we enbedded dict inside a list 
data3 = [
  { "name": "Amy", "address": "Apple st 652" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean blvd 2" },
  { "name": "Betty", "address": "Green Grass 1" },
  { "name": "Richard", "address": "Sky st 331" },
  { "name": "Susan", "address": "One way 98" },
  { "name": "Vicky", "address": "Yellow Garden 2" },
  { "name": "Ben", "address": "Park Lane 38" },
  { "name": "William", "address": "Central st 954" },
  { "name": "Chuck", "address": "Main Road 989" },
  { "name": "Viola", "address": "Sideway 1633" }
]

coll_create.insert_many(data3)


list_of_records = [
    {'companyName': 'studio ghibli',
     'product': 'anime films',
     'popular film': 'Spirited Away'},
    
    {'companyName': 'P.A.N',
     'product': 'Colombian Corn Flour',
     'courseOffered': 'Cocina para principiantes'},
    
    {'companyName': 'Kleenex',
     'product': 'Tissues',
     'courseOffered': 'Prevet desieases'}
]

coll_create.insert_many(list_of_records)

random_data = [
    {'_id': '9', 'companyName1': 'Peluches', 'Faculty': 'XYZ'},
    {'_id': '10', 'companyName2': 'Pinturas', 'Faculty': 'ABC'},
    {'_id': '11', 'companyName3': 'Parques', 'Faculty': 'PQR'},
]


existing_document = coll_create.find_one({'_id': '6'})
if existing_document:
    print(f"Document with _id '6' already exists: {existing_document}")
else:
    pass




# # ////////////////// Quering our collections in python ////////////////////////////////////////
# 

# In[42]:


for i in coll_create.find():
    print(i)



# In[37]:


# If we want to fetch only one record

coll_create.find_one()


# In[38]:


from collections import defaultdict

# Create a dictionary to store unique document values
unique_documents = defaultdict(list)

# Iterate through the collection and filter out duplicates
for doc in coll_create.find():
    if 'companyName' in doc:
        key = (doc.get('companyName'), doc.get('product'), doc.get('courseOffered'))
    else:
        key = (doc.get('name'),)  # Only use 'name' for data3 documents
    unique_documents[key].append(doc)

# Remove duplicates by keeping only the first occurrence of each set of values
for key, docs in unique_documents.items():
    if len(docs) > 1:
        # Keep the first document, remove the rest
        for doc in docs[1:]:
            coll_create.delete_one({'_id': doc['_id']})


# In[39]:


for i in coll_create.find({'companyName': 'P.A.N'}):
    print(i)


# In[40]:


for i in coll_create.find({'_id':{'$gte':'4'}}):
    print(i)


# In[41]:


# If we want to replace one feature for the other

coll_create.update_many({'companyName':'P.A.N'}, {'$set': {'companyName':'Holly Flour'}})


# In[ ]:


# If we want to drop the entire collection

# coll_create.drop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




