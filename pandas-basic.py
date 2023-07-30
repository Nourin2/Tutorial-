#!/usr/bin/env python
# coding: utf-8

# # Pandas
# 
# 
libraries
# In[2]:


import pandas as pd
import numpy as np


# In[3]:


import numpy as np


# In[4]:


df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['Column1','Column2','Column3','Column4'])


# In[5]:


df.head()


# In[6]:


df.to_csv('Test1.csv')


# In[7]:


#Accessin the elements 
##1. .loc  2. .iloc
df.loc['Row1']


# In[8]:


## check the type
type(df.loc['Row1'])


# In[9]:


df.iloc[:,:]


# In[10]:


df.iloc[0:2,0:1]


# In[11]:


## take the elements from the column 
df.iloc[:,1:]


# In[12]:


## convert dataframe into array
df.iloc[:,1:].values


# In[13]:


df.iloc[:,1:].values.shape


# In[14]:


df['Column1'].value_counts()


# In[15]:


## how to check the null condition
df.isnull().sum()


# In[16]:


# uniqye value show
df['Column1'].unique()


# In[18]:


df=pd.read_csv('Test Data - nazim.csv')


# In[19]:


df.head()


# In[20]:


df.info()


# In[21]:


df.describe()


# In[22]:


# Get unique character count
df['Frequency'].value_counts()


# In[24]:


df.corr()


# In[ ]:




