#!/usr/bin/env python
# coding: utf-8

# # Working w Python and MySQL continued 📅👩‍💻

# In[6]:


import mysql.connector 

cnx = mysql.connector.connect(host='localhost',
    user='root',
    password='@#Marimo04',
    database='monidb1')

# help to run query
cursor = cnx.cursor()

print(cursor)

cursor.execute('CREATE TABLE if not exists monidb.test_table (c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))')



# In[20]:


import mysql.connector
db = mysql.connector.connect(
host='localhost',
user='root',
password='@#Marimo04')
    
# help to run query

print(db)
mycursor = db.cursor()
mycursor.execute('CREATE TABLE if not exists test2.test_table (c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))')
db.close()

# inserting data

mycursor.execute('insert into test2.test_table values(1372, 'moni', 234, 819.32, 'guevara')')
db.commit()
db.close()




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




