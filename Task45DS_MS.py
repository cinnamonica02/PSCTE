#!/usr/bin/env python
# coding: utf-8

# # Mongo DB & Python Continued 😭

# In[28]:


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



# In[46]:


import pymongo
from pymongo import MongoClient
import datetime


# Creating our Database

# Creating our Database

db = client['ProductivityLog']

# Creating our Collection

coll_create = db['Plog_details']

todo1 = {
    'name': 'Lena',
    'text': 'Get back to team feedback on code',
    'status': 'open',
    'tags': ['python', 'coding'],
    'date': datetime.datetime.utcnow()
}

# Inserting data 

# result = coll_create.insert_one(todo1)

todo2 = [{
    'name': 'Juan',
    'text': 'Team Meeting',
    'status': 'open',
    'tags': ['proyect management', 'feedback'],
    'date': datetime.datetime(2023, 8, 8, 7, 21)
}]

# result = coll_create.insert_many(todo2)




# ## Retrieving items in our collections

# In[30]:


result = coll_create.find_one()
print(result)


# In[31]:


# query for specific fields

results = coll_create.find_one({'name': 'Juan','text': 'Team Meeting'})
print(result)


# In[32]:


# iterating

print(list(results))
for result in results:
    print(result)


# In[33]:


# quering for list items

result = coll_create.find_one({'tags': 'feedback'})
print(result)


# In[34]:


# Quering for specific id - since ids are stored as objid so we must do this:

from bson.objectid import ObjectId
result = coll_create.find_one({'_id': ObjectId('64d2517bae1e2bdaff7f173d')})
print(result)


# In[40]:


# Counting Docs

print(coll_create.count_documents({}))


# In[48]:


# range queries and sorting

d = datetime.datetime(2023, 8, 8)
results = coll_create.find({'date': {'$gt': d}}).sort('name')
for result in results:
    print(result)


# ### Different Quering dcmt PyMongo
# 
# https://www.mongodb.com/docs/manual/reference/operator/query/

# In[53]:


from bson.objectid import ObjectId
result = coll_create.delete_one({'_id':ObjectId('64d2510bae1e2bdaff7f173c')})


# In[ ]:


# if you want to delete all at once

# result = coll_create.delete_many({})/


# In[55]:


# if you want to update items:
result = coll_create.update_one({'tags': 'python'}, {'$set': {'status': 'done'}})


# In[57]:


# if you want to unset 
result = coll_create.update_one({'tags': 'python'}, {'$unset': {'status': 'None'}})

# and then set it again it will add it to the doc :)

result = coll_create.update_one({'tags': 'python'}, {'$set': {'status': 'new open'}})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




