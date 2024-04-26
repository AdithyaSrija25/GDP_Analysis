#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('gdp.csv')
df.head()


# In[4]:


df.isnull().sum()


# In[5]:


df['Country Name'].describe()


# In[6]:


df['Country Code'].describe()


# In[ ]:


## Analysing Arab World


# In[7]:


df_pr = df[df['Country Name'] == 'Arab World']
df_pr.plot(kind = 'line', x = 'Year', y = 'Value',
           figsize = (15,6),
           legend = False,
           grid = True,
           ylabel = 'GDP',
           xlabel = 'YEARS')


# In[8]:


df_pr


# In[9]:


data = df_pr.values

gdp_change = [0]

for i in range(1,len(data)):
    
    prev = data[i-1][3]
    cur = data[i][3]
    
    gdp_change.append(round(((cur - prev) / prev)*100,2))


# In[10]:


df_pr.assign(GDP = gdp_change)


# In[ ]:




