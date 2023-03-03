#!/usr/bin/env python
# coding: utf-8

# In[5]:


## NUMPY
## Generate a 2 by 3 matrix containing elements from 1 to 6 and multiply it by a scaler of two.
import numpy as np
# creating a 2 by 3 matrix
matrix = np.array([[1,2,3],[4,5,6]])
matrix


# In[8]:


# multiply it by a scaler of two.
scaler = 2 * matrix
print(scaler)


# In[9]:


# Create a 3 by 3 identity matrix
identity_matrix = np.array([[1,0,0],[0,1,0],[0,0,1]])
identity_matrix


# In[14]:


#Create a 1-D array call arry1 which 
arry1 = np.arange(27)
print(arry1)


# In[17]:


arry2 = arry1.reshape(3,3,3)
print(arry2)


# In[18]:


# Create two 2-D arrays with the first array containing elements from 1 to 6. 
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])


# In[19]:


print(arr1)


# In[20]:


print(arr2)


# In[21]:


# horizontal stack
horizontal_stack = np.hstack((arr1,arr2))
horizontal_stack


# In[22]:


# vertical stack
vertical_stack = np.vstack((arr1,arr2))
vertical_stack 


# In[23]:


# Create an equally spaced sequence with a gap of 5 ranging from 0 to 100
sequence = np.arange(0,101,5)
sequence


# In[24]:


# PANDAS
# Create a DataFrame named as students using a list of names of 5 students.
import pandas as pd


# In[29]:


students = pd.DataFrame(['Benunai','Alexis','Ewurabena','Israel','Bamba'])
students


# In[4]:


# Write a program to create a DataFrame teams using a list of names of Ghana Premier League Teams 
# and the goals they scored in their previous five matches.
import pandas as pd
teams = pd.DataFrame({'Name': ['Hearts Of Oak','Kotoko','Elmina Sharks','King Faisal','Great Olympics','Aduana Stars'],'Goals': [49,38,30,24,12,12]})
teams


# In[7]:


# Write a program to create a DataFrame countries using a dictionary which stored country name, capitals, 
# and populations of the country. Do this for West African Countries.
import pandas as pd
countries = pd.DataFrame({'Country': ['Ghana','Mali','Togo','Sierra Leon','Nigeria','Burkina Faso'], 'Capital': ['Accra','Bamako','Lome','Freetown','Abuja','Yuagaduogu'], 'Population': [3435600,347700,3456200,341600,346800,345460]})
countries


# In[4]:


# Final assignment 
import pandas as pd
league_table = pd.DataFrame({'Team': ['Hearts of Oak','Asante Kotoko','Ebusua Dwarfs','Sekondi Hassacas','Okwahu United','Tano Bofoakwa','BA United'],'GF':[120,90,90,80,78,70,71],'GA':[35,55,60,43,39,50,55],'PTS':[80,60,60,55,53,49,44]})
league_table


# In[ ]:




