#!/usr/bin/env python
# coding: utf-8

# # Best practice exception handling 👍

# ##  use always a specific exception :D
# 

# In[1]:


# Wrong way example

try:
    10/0
except Exception as e:
    print(e)


# In[2]:


# Right way example
try:
    10/0
except ZeroDivisionError as e:
    print(e)


# In[3]:


# Print always a valid msg

try:
    10/0
except ZeroDivisionError as e:
    print('This is my zero division error I am handling')


# ## Always try to log 

# In[5]:


import logging
logging.basicConfig(filename = 'error.log', level = logging.ERROR)
try:
    10/0
except ZeroDivisionError as e:
    logging.error('this is my zero division error I am handling {}'.format(e))


# ## Always avoid to write multiple exception handling

# In[7]:


# for eg
try:
    10/0
except FileNotFoundError as e:
    logging.error('this is my file not found error I am handling {}'.format(e))
except AttributeError as e:
    logging.error('this is my attribute error I am handling {}'.format(e))
except ZeroDivisionError as e:
    logging.error('this is my zero division error I am handling {}'.format(e))
        
    


# ## Prepare propper documentation!
# 

# ## Clean up all the resources 🫧🧼
# 

# In[10]:


# We have to both open and close propperly so we make sure
## we are not over or under utilizing our resources!

try:
    with open('test.txt', 'w') as f:
        f.write('this is my msg to file')
except FileNotFoundError as e:
    logging.error('this is my file not found {}'.format(e))
finally:
    f.close()


# In[ ]:




