#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# ## Import the initial csv file

# In[3]:


df = pd.read_csv('C:\\Users\\1\\Desktop\\Spidey Dis\\p\\TRD.csv', encoding='utf-8')


# In[4]:


df.head(5)


# In[5]:


df.isnull().sum()


# ### [all frequency] duplicate entries in the 'StockID' column

# In[6]:


stock_count = df['Stock'].value_counts(ascending=False)


# #### Print each Stock number and its frequency on two columns respectively, the left column is the Stock number, and the right column is the frequency

# In[7]:


stock_count.head()
# Name: Stock, Length: 2966, dtype: int64


# ### [frequency >= 15] duplicate entries in the 'StockID' column

# #### Convert stock_count list to dataframe

# In[8]:


stock_df = pd.DataFrame(stock_count)


# In[9]:


stock_df.head()


# ####  Create a dataframe containing stock numbers with a frequency greater than or equal to 15 times and their frequency

# In[10]:


stock_15_df = stock_df[stock_df['Stock'] >= 15] 


# In[11]:


stock_15_df


# ####  Create an empty dataframe

# In[12]:


new_df = pd.DataFrame()


# ####  Print out the index value in the stock_15_df dataframe as a list

# In[13]:


stock_index = stock_15_df.index.values


# In[14]:


stock_index


# ####  Write each stock with a frequency greater than or equal to 15 in the new dataframe

# In[15]:


for i in stock_index:
    filter_df = df.loc[df['Stock'] == i]
    new_df = pd.concat([filter_df, new_df], ignore_index=True)


# In[16]:


new_df.head()


# ####  new dataframe (df_Rt) only retains the four columns Index and Stock, TrdMon, Rt-ft

# In[17]:


df_Rt = new_df.drop(columns=['CloMon', 'Rt', 'ft'])


# In[18]:


df_Rt.head()


# #### df_Rt adds RiskPremium, SMB, HML three columns on the original basis, and assigns null values

# In[19]:


df_Rt[['RiskPremium','SMB','HML']] = df.apply(lambda x:('','',''), axis=1, result_type='expand')


# In[20]:


df_Rt


# ##  Add the three columns of data in ff_data.csv to stock_data.csv (when TradingMonth is the same)
def read_data(file):
    data = pd.read_csv(file)
    return data

def merge_data(f1, f2):
    data1 = pd.read_csv(f1)
    data2 = pd.read_csv(f2)
    
    for i in range(len(data1)):
        date = data1['TrdMon'][i]
        row2 = data2[data2['TrdMon'].isin([date])]
        data1['RiskPremium'][i] = row2['RiskPremium']
        data1['SMB'][i] = row2['SMB']
        data1['HML'][i] = row2['HML']
    data1.to_csv('new.csv', header=1, index=0)

if __name__ == '__main__':
    merge_data('stock_data.csv', 'ff_data.csv')
# ### 返回Stock列中不相同的项

# In[21]:


stock_df


# In[22]:


stock_df.head(20)


# In[24]:


stock_df.to_csv('stock_list.csv', header=1, index=1)


# In[ ]:




