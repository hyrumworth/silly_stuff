#!/usr/bin/env python
# coding: utf-8

# In[275]:


import pandas as pd
from bs4 import BeautifulSoup


# In[409]:





# In[ ]:


master_df = pd.DataFrame(columns= ['date','attendance','promotion','card name','location'])


# In[453]:


data = pd.read_html('http://www.profightdb.com/cards-with-highest-attendance-pg30.html') # just run this a few times and 
# switch out the pg1 with pg2, pg3 4 etc. 
df = data[0]
frames = [master_df,df]
master_df = pd.concat(frames)
master_df


# In[ ]:




