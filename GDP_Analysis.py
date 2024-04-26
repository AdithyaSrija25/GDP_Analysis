#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import os
import plotly.express as px
import plotly.offline as pyo
df = pd.read_csv('gdp.csv')
df.head()


# In[21]:


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


# In[3]:


df_pr = df[df['Country Name'] == 'World']

fig = px.line(df_pr, x = 'Year', y = 'Value', title = 'World GDP Analysis')

fig


# In[6]:


df_pr = df[df['Country Name'] == 'India']

fig = px.line(df_pr, x = 'Year', y = 'Value', title = 'Indian GDP Analysis')
fig

