#!/usr/bin/env python
# coding: utf-8

# In[156]:


import os, shutil


# In[157]:


path = r'C:/Users/akhil/Documents/sorter/'


# In[158]:


file_name = os.listdir(path)


# In[159]:


folder_name = ['excel files','image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
            os.makedirs(path +folder_name[loop])


# In[160]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "/excel files" + file):
        shutil.move(path + file, path + "/excel files/" + file)
    elif ".PNG" in file and not os.path.exists(path + "/image files" + file):
        shutil.move(path + file, path + "/image files/" + file)
    elif ".JPG" in file and not os.path.exists(path + "/image files" + file):
        shutil.move(path + file, path + "/image files/" + file)
    elif ".docx" in file and not os.path.exists(path + "/text files" + file):
        shutil.move(path + file, path + "/text files/" + file)
    

