#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data =pd.read_csv("DATASETSALARY.csv")


# In[3]:


data


# In[4]:


plt.figure(figsize=(8, 6))
plt.hist(data['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[5]:


plt.figure(figsize=(8, 6))
plt.scatter(data['Experience'], data['Salary'], color='blue', alpha=0.5)
plt.title('Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.show()


# In[6]:


plt.figure(figsize=(8, 6))
sns.boxplot(data=data)
plt.title('Boxplot of Salary Prediction')
plt.xlabel('Emp Detail')
plt.ylabel('Salary')
plt.show()


# In[ ]:




