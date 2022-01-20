#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r'Food.csv', encoding='latin-1')


# In[3]:


df.shape


# In[4]:


df


# In[5]:


df.describe(include='all')


# In[6]:


df.isnull().sum()


# In[82]:


df.Area.unique().size


# In[8]:


df.duplicated().any()


# In[19]:


lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]

col = ['Age','Nationality','Overall']

df1 = pd.DataFrame(lst, columns=col, index=[i for i in range(1,4)])


# In[20]:


df1


# In[61]:


df.groupby('Item')['Item'].count()
df[['Item']] = df[['Item']].fillna(value='mcf')


# In[62]:


df.isnull().sum()


# In[63]:


df.groupby('Item')['Item'].count()


# In[83]:


df.groupby('Y2014')['Y2014'].count()
df.groupby('Y2017')['Y2017'].count()

df.groupby('Item')


# In[77]:


df['mean'] = df.mean(axis=1)


# In[78]:


df


# In[80]:


df['std'] = df.std(axis=1)


# In[81]:


df


# In[87]:


df.groupby('Y2018')['Element'].count()

df.groupby('Element').first()


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




