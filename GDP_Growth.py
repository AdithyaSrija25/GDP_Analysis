#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('gdp.csv')
df.head()


# In[ ]:


##Finding gdp growth of a country


# In[2]:


df_pr = df[df['Country Name'] == 'Arab World']

data = df_pr.values

gdp_change = [0]

for i in range(1,len(data)):
    
    prev = data[i-1][3]
    cur = data[i][3]
    
    gdp_change.append(round(((cur - prev) / prev)*100,2))
    
df_pr = df_pr.assign(GDP = gdp_change)


# In[ ]:


##Finding gdp growth of every country


# In[3]:


final_data = []

for country_name in df['Country Name'].unique():
    
    df_pr = df[df['Country Name'] == country_name]

    data = df_pr.values
    gdp_change = [0]

    for i in range(1,len(data)):

        prev = data[i-1][3]
        cur = data[i][3]

        gdp_change.append(round(((cur - prev) / prev)*100,2))

    df_pr = df_pr.assign(GDP = gdp_change)
    final_data.append(df_pr)
df = pd.concat(final_data, axis = 0)
df.head()


# In[4]:


df.groupby('Country Name').max()['Value'].sort_values(ascending = False).head(50)


# In[ ]:




