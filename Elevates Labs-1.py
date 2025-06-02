#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

file_path = "Netflix_movies_and_tv_shows_clustering.csv"
df = pd.read_csv(file_path)

print("Initial dataset shape:", df.shape)
df.head()


# In[2]:


print("\nMissing values per column:")
print(df.isnull().sum())

df_cleaned = df.dropna()

print("\nAfter handling missing values:", df_cleaned.shape)


# In[3]:


df_cleaned = df_cleaned.drop_duplicates()
print("After removing duplicates:", df_cleaned.shape)


# In[4]:


df_cleaned['type'] = df_cleaned['type'].str.strip().str.lower()

df_cleaned['country'] = df_cleaned['country'].str.strip().str.title()


# In[5]:


df_cleaned['date_added'] = pd.to_datetime(df_cleaned['date_added'], errors='coerce')

df_cleaned['date_added'] = df_cleaned['date_added'].dt.strftime('%d-%m-%Y')

df_cleaned[['date_added']].head()


# In[6]:


df_cleaned.columns = df_cleaned.columns.str.lower().str.replace(' ', '_')

print("Renamed columns:", df_cleaned.columns.tolist())


# In[7]:


df_cleaned['release_year'] = df_cleaned['release_year'].astype('int', errors='ignore')

print("\nData types after conversion:")
print(df_cleaned.dtypes)


# In[ ]:


df_cleaned.to_csv('cleaned_netflix_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_netflix_data.csv'")

