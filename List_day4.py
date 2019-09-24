#!/usr/bin/env python
# coding: utf-8

# In[1]:


#introduction to List
#List is a collection of items in an order
#List is mutable datatype -> it can be modified when it is assigned.
bicycle = [ 'ranger', 'hero', 'redline','trek']
print(bicycle)


# In[9]:


#How to access elements in a list
# 2nd position -> index =1 as stats with 0
print(bicycle[1])

print(bicycle[-1])  #Reverse index = -1 for last element

# 2 ways of accesing last element -> +ve index & -ve(reverse) index


# In[11]:


#enhancing the list
print(bicycle[0].title())  #Make as starting with caps using title().


# In[14]:


message = "my first bicycle was a {bicycle[1].title()}"
print(message)


# In[20]:


#modify elemt of a lis
bikes = ['honda','yamaha','bajaj']
print(bikes[0])
# honda changed to ducati
bikes[0]= 'ducati'
print(bikes)
         


# In[ ]:




