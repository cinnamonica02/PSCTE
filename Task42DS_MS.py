#!/usr/bin/env python
# coding: utf-8

# # Using Python and MySQL 📅👩‍💻

# In[3]:


import mysql.connector 

cnx = mysql.connector.connect(host='localhost',
    user='root',
    password='@#Marimo04',
    database='monidb1')

# help to run query
cursor = cnx.cursor()

print(cursor)

# Quering our table :3

query = ('select id, name1 from monidb1.studenttable')

cursor.execute(query)

# Printing values of the query
for (id, name1) in cursor:
    print(id, name1)

cursor.close()
cnx.close()


# In[6]:


### Creating a new table and inserting Data
import mysql.connector 

cnx = mysql.connector.connect(host='localhost',
    user='root',
    password='@#Marimo04',
    database='monidb')

cursor = cnx.cursor()

# cursor.execute('CREATE TABLE monidb.mytable02 (name VARCHAR(100), location VARCHAR(100))')

insertquery = 'INSERT INTO monidb.mytable02 (name, location) VALUES (%s, %s)'
value = ('Anna', 'Warsaw')

cursor.execute(insertquery, value)

### Insert multiple records in Table
multipleinsertquery = 'INSERT INTO mytable02 (name, location) VALUES (%s, %s)'
values = [('Adam', 'Estonia'),
          ('Pristen', 'US'),
          ('Alejandra', 'Colombia'),
          ('Kira', 'Korea')]
cursor.executemany(multipleinsertquery, values)

cursor = cnx.cursor()
cursor.execute('Select * from mytable02')

# Fetching the data 

# 1 - using forloop as seen in prev ex
# 2 - using cursor.ferchall() to fetch all results from table

cursor.fetchall()


# In[ ]:


# If we want to drop the table we created - execute the following command


# cursor.execute('DROP table mytable02')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




