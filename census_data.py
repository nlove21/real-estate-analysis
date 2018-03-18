
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from census import Census
import seaborn as sns
get_ipython().magic('matplotlib inline')

# Census API Key
from localenv import census_api_key


# In[2]:


# Load census daya 2011 - 2015

c11 = Census(census_api_key, year=2011)
c12 = Census(census_api_key, year=2012)
c13 = Census(census_api_key, year=2013)
c14 = Census(census_api_key, year=2014)
c15 = Census(census_api_key, year=2015)


# In[3]:


census_data11 = c11.acs5.get(("NAME", 
                          "B19013_001E", 
                          "B01003_001E", 
                          "B01002_001E",
                          "B23025_005E", 
                          "B25058_001E", 
                          "B25077_001E"), {'for': 'state:*'})

census_data12 = c12.acs5.get(("NAME", 
                          "B19013_001E", 
                          "B01003_001E", 
                          "B01002_001E",
                          "B23025_005E",
                          "B25058_001E", 
                          "B25077_001E"), {'for': 'state:*'})

census_data13 = c13.acs5.get(("NAME", 
                          "B19013_001E", 
                          "B01003_001E", 
                          "B01002_001E",
                          "B23025_005E", 
                          "B25058_001E", 
                          "B25077_001E"), {'for': 'state:*'})

census_data14 = c14.acs5.get(("NAME", 
                          "B19013_001E", 
                          "B01003_001E", 
                          "B01002_001E",
                          "B23025_005E", 
                          "B25058_001E", 
                          "B25077_001E"), {'for': 'state:*'})

census_data15 = c15.acs5.get(("NAME", 
                          "B19013_001E", 
                          "B01003_001E", 
                          "B01002_001E",
                          "B23025_005E", 
                          "B25058_001E", 
                          "B25077_001E"), {'for': 'state:*'})


# In[4]:


# Convert to DataFrame
census_pd11 = pd.DataFrame(census_data11)

# Column Reordering
census_pd11 = census_pd11.rename(columns={"B01003_001E": "Population (2011)",
                                      "B01002_001E": "Median Age (2011)",
                                      "B19013_001E": "Household Income (2011)",
                                      "B23025_005E": "Unemployment Count (2011)",
                                      "B25058_001E": "Median Rent (2011)",
                                      "B25077_001E": "Median Home Value (2011)",
                                      "NAME": "Name", 
                                      "state": "State"})

# Add in Employment Rate (Employment Count / Population)
census_pd11["Unemployment Rate (2011)"] = 100 *     census_pd11["Unemployment Count (2011)"].astype(
        int) / census_pd11["Population (2011)"].astype(int)

# Final DataFrame
census_pd11 = census_pd11[["State", "Name", "Population (2011)", "Median Age (2011)", "Household Income (2011)", 
                           "Unemployment Rate (2011)", "Median Rent (2011)", "Median Home Value (2011)"]]

census_pd11.head()


# In[5]:


# Convert to DataFrame
census_pd12 = pd.DataFrame(census_data12)

# Column Reordering
census_pd12 = census_pd12.rename(columns={"B01003_001E": "Population (2012)",
                                      "B01002_001E": "Median Age (2012)",
                                      "B19013_001E": "Household Income (2012)",
                                      "B23025_005E": "Unemployment Count (2012)",
                                      "B25058_001E": "Median Rent (2012)",
                                      "B25077_001E": "Median Home Value (2012)", 
                                      "NAME": "Name (2012)", 
                                      "state": "State (2012)"})

# Add in Employment Rate (Employment Count / Population)
census_pd12["Unemployment Rate (2012)"] = 100 *     census_pd12["Unemployment Count (2012)"].astype(
        int) / census_pd12["Population (2012)"].astype(int)

# Final DataFrame
census_pd12 = census_pd12[["Name (2012)", "State (2012)", "Population (2012)", "Median Age (2012)", "Household Income (2012)", "Unemployment Rate (2012)", "Median Rent (2012)", "Median Home Value (2012)"]]

census_pd12.head()


# In[6]:


# Convert to DataFrame
census_pd13 = pd.DataFrame(census_data13)

# Column Reordering
census_pd13 = census_pd13.rename(columns={"B01003_001E": "Population (2013)",
                                      "B01002_001E": "Median Age (2013)",
                                      "B19013_001E": "Household Income (2013)",
                                      "B23025_005E": "Unemployment Count (2013)",
                                      "B25058_001E": "Median Rent (2013)",
                                      "B25077_001E": "Median Home Value (2013)", 
                                      "NAME": "Name (2013)", 
                                      "state": "State (2013)"})

# Add in Employment Rate (Employment Count / Population)
census_pd13["Unemployment Rate (2013)"] = 100 *     census_pd13["Unemployment Count (2013)"].astype(
        int) / census_pd13["Population (2013)"].astype(int)

# Final DataFrame
census_pd13 = census_pd13[["Name (2013)", "State (2013)", "Population (2013)", "Median Age (2013)", "Household Income (2013)", "Unemployment Rate (2013)", "Median Rent (2013)", "Median Home Value (2013)"]]

census_pd13.head()


# In[7]:


# Convert to DataFrame
census_pd14 = pd.DataFrame(census_data14)

# Column Reordering
census_pd14 = census_pd14.rename(columns={"B01003_001E": "Population (2014)",
                                      "B01002_001E": "Median Age (2014)",
                                      "B19013_001E": "Household Income (2014)",
                                      "B23025_005E": "Unemployment Count (2014)",
                                      "B25058_001E": "Median Rent (2014)",
                                      "B25077_001E": "Median Home Value (2014)", 
                                      "NAME": "Name (2014)", 
                                      "state": "State (2014)"})

# Add in Employment Rate (Employment Count / Population)
census_pd14["Unemployment Rate (2014)"] = 100 *     census_pd14["Unemployment Count (2014)"].astype(
        int) / census_pd14["Population (2014)"].astype(int)

# Final DataFrame
census_pd14 = census_pd14[["Name (2014)", "State (2014)", "Population (2014)", "Median Age (2014)", "Household Income (2014)", "Unemployment Rate (2014)", "Median Rent (2014)", "Median Home Value (2014)"]]

census_pd14.head()


# In[8]:


# Convert to DataFrame
census_pd15 = pd.DataFrame(census_data15)

# Column Reordering
census_pd15 = census_pd15.rename(columns={"B01003_001E": "Population (2015)",
                                      "B01002_001E": "Median Age (2015)",
                                      "B19013_001E": "Household Income (2015)",
                                      "B23025_005E": "Unemployment Count (2015)",
                                      "B25058_001E": "Median Rent (2015)", 
                                      "B25077_001E": "Median Home Value (2015)", 
                                      "NAME": "Name (2015)", 
                                      "state": "State (2015)"})

# Add in Employment Rate (Employment Count / Population)
census_pd15["Unemployment Rate (2015)"] = 100 *     census_pd15["Unemployment Count (2015)"].astype(
        int) / census_pd15["Population (2015)"].astype(int)

# Final DataFrame
census_pd15 = census_pd15[["Name (2015)", "State (2015)", "Population (2015)", "Median Age (2015)", "Household Income (2015)", "Unemployment Rate (2015)", "Median Rent (2015)", "Median Home Value (2015)"]]

census_pd15.head()


# In[9]:


#merging 2011-2012
census_merge1112 = pd.merge(census_pd11, census_pd12, left_index=True, right_index=True, how='outer')
census_merge1112.rename(index=str, columns={"Name":"State"})
dropColumns = ["State (2012)", "Name (2012)"]
census_merge1112.drop(dropColumns, inplace=True, axis=1)
census_merge1112.head()


# In[10]:


#merging 2011-2013
census_merge111213 = pd.merge(census_merge1112, census_pd13, left_index=True, right_index=True, how='outer')
dropColumns = ["State (2013)", "Name (2013)"]
census_merge111213.drop(dropColumns, inplace=True, axis=1)
census_merge111213.head()


# In[11]:


#merging 2011-2014
census_merge11121314 = pd.merge(census_merge111213, census_pd14, left_index=True, right_index=True, how='outer')
dropColumns = ["State (2014)", "Name (2014)"]
census_merge11121314.drop(dropColumns, inplace=True, axis=1)
census_merge11121314.head()


# In[12]:


#final merge years 2011-2015
census_2011_2015 = pd.merge(census_merge11121314, census_pd15, left_index=True, right_index=True, how='outer')
dropColumns = ["State", "State (2015)", "Name (2015)"]
census_2011_2015.drop(dropColumns, inplace=True, axis=1)
census_2011_2015.head()


# In[13]:


# 50 states plot for Median Age v. Population

census_2011_2015_50States = census_2011_2015.set_index("Name")

census_2011_2015_50States["Population (2015)"] = pd.to_numeric(census_2011_2015_50States["Population (2015)"])
census_2011_2015_50States["Median Age (2015)"] = pd.to_numeric(census_2011_2015_50States["Median Age (2015)"])
census_2011_2015_50States["Population (2014)"] = pd.to_numeric(census_2011_2015_50States["Population (2014)"])
census_2011_2015_50States["Median Age (2014)"] = pd.to_numeric(census_2011_2015_50States["Median Age (2014)"])
census_2011_2015_50States["Population (2013)"] = pd.to_numeric(census_2011_2015_50States["Population (2013)"])
census_2011_2015_50States["Median Age (2013)"] = pd.to_numeric(census_2011_2015_50States["Median Age (2013)"])
census_2011_2015_50States["Population (2012)"] = pd.to_numeric(census_2011_2015_50States["Population (2012)"])
census_2011_2015_50States["Median Age (2012)"] = pd.to_numeric(census_2011_2015_50States["Median Age (2012)"])
census_2011_2015_50States["Population (2011)"] = pd.to_numeric(census_2011_2015_50States["Population (2011)"])
census_2011_2015_50States["Median Age (2011)"] = pd.to_numeric(census_2011_2015_50States["Median Age (2011)"])
#census_2011_2015["State"] = pd.to_numeric(census_2011_2015["State"])


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 20
fig_size[1] = 33
plt.rcParams["figure.figsize"] = fig_size


ax = census_2011_2015_50States.plot.scatter(x='Population (2015)', y='Median Age (2015)', label='2015', color = 'DarkRed', s=60)
census_2011_2015_50States.plot.scatter(x='Population (2014)', y='Median Age (2014)', label='2014', color='DarkBlue', s=60, ax=ax)
census_2011_2015_50States.plot.scatter(x='Population (2013)', y='Median Age (2013)', label='2013', color='DarkGreen', s=60, ax=ax)
census_2011_2015_50States.plot.scatter(x='Population (2012)', y='Median Age (2012)', label='2012', color='Red', s=60, ax=ax)
census_2011_2015_50States.plot.scatter(x='Population (2011)', y='Median Age (2011)', label='2011', color='Green', s=60, ax=ax)

plt.savefig("PopulationVersusAge.png")
plt.show()


# In[14]:


# 5 states plot for Unemployment Rate v. Population

census_2011_2015_5States= census_2011_2015.drop([0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 47, 48, 49, 50, 51])

census_2011_2015_5States["Population (2015)"] = pd.to_numeric(census_2011_2015_5States["Population (2015)"])
census_2011_2015_5States["Population (2014)"] = pd.to_numeric(census_2011_2015_5States["Population (2014)"])
census_2011_2015_5States["Population (2013)"] = pd.to_numeric(census_2011_2015_5States["Population (2013)"])
census_2011_2015_5States["Population (2012)"] = pd.to_numeric(census_2011_2015_5States["Population (2012)"])
census_2011_2015_5States["Population (2011)"] = pd.to_numeric(census_2011_2015_5States["Population (2011)"])
census_2011_2015_5States["Unemployment Rate (2015)"] = pd.to_numeric(census_2011_2015_5States["Unemployment Rate (2015)"])
census_2011_2015_5States["Unemployment Rate (2014)"] = pd.to_numeric(census_2011_2015_5States["Unemployment Rate (2014)"])
census_2011_2015_5States["Unemployment Rate (2013)"] = pd.to_numeric(census_2011_2015_5States["Unemployment Rate (2013)"])
census_2011_2015_5States["Unemployment Rate (2012)"] = pd.to_numeric(census_2011_2015_5States["Unemployment Rate (2012)"])
census_2011_2015_5States["Unemployment Rate (2011)"] = pd.to_numeric(census_2011_2015_5States["Unemployment Rate (2011)"])

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size

ex = census_2011_2015_5States.plot.scatter(x='Population (2015)', y='Unemployment Rate (2015)', label='2015', color = 'DarkRed', s=60)
census_2011_2015_5States.plot.scatter(x='Population (2014)', y='Unemployment Rate (2014)', label='2014', color='DarkBlue', s=60, ax=ex)
census_2011_2015_5States.plot.scatter(x='Population (2013)', y='Unemployment Rate (2013)', label='2013', color='DarkGreen', s=60, ax=ex)
census_2011_2015_5States.plot.scatter(x='Population (2012)', y='Unemployment Rate (2012)', label='2012', color='Red', s=60, ax=ex)
census_2011_2015_5States.plot.scatter(x='Population (2011)', y='Unemployment Rate (2011)', label='2011', color='Green', s=60, ax=ex)


# In[15]:


# # ADDING IN STATE ABBREVS TO CHART - IN PROGRESS

# st2015=['','','','','CA','CO','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','OR','','','','SD','','TX','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

# for line in range(0,census_2011_2015_5States.shape[0]):
#     ex.text(census_2011_2015_5States['Population (2015)'][line]+1.1,census_2011_2015_5States['Unemployment Rate (2015)'][line], st2015[line], weight='bold')


# In[16]:


# Household Income plot - MAY DELETE

census_2011_2015_5Statess = census_2011_2015_5States.drop(["Population (2011)", 
                                "Median Age (2011)", 
                                "Unemployment Rate (2011)", 
                                "Median Rent (2011)", 
                                "Median Home Value (2011)", 
                                "Population (2012)", 
                                "Median Age (2012)", 
                                "Unemployment Rate (2012)", 
                                "Median Rent (2012)", 
                                "Median Home Value (2012)", 
                                "Population (2013)", 
                                "Median Age (2013)",  
                                "Unemployment Rate (2013)", 
                                "Median Rent (2013)", 
                                "Median Home Value (2013)", 
                                "Population (2014)", 
                                "Median Age (2014)",  
                                "Unemployment Rate (2014)", 
                                "Median Rent (2014)", 
                                "Median Home Value (2014)",  
                                "Population (2015)", 
                                "Median Age (2015)",
                                "Unemployment Rate (2015)", 
                                "Median Rent (2015)", 
                                "Median Home Value (2015)"], axis=1)

census_2011_2015_5Statess.plot(subplots=True, figsize=(8, 8)); plt.legend(loc='best')


# In[17]:


# Adding in Year columns

# amended 2011 code above
census_pd11s = pd.DataFrame(census_data11)
census_pd11s = census_pd11s.rename(columns={"B01003_001E": "Population",
                                      "B01002_001E": "Median Age",
                                      "B19013_001E": "Household Income",
                                      "B23025_005E": "Unemployment Count",
                                      "B25058_001E": "Median Rent",
                                      "B25077_001E": "Median Home Value",
                                      "NAME": "Name", 
                                      "state": "State"})
census_pd11s["Unemployment Rate"] = 100 *     census_pd11s["Unemployment Count"].astype(
        int) / census_pd11s["Population"].astype(int)
census_pd11s = census_pd11s[["State", "Name", "Population", "Median Age", "Household Income", "Unemployment Rate", "Median Rent", "Median Home Value"]]
census_pd11s["Year"] = "2011"


# amended 2012 code above
census_pd12s = pd.DataFrame(census_data12)
census_pd12s = census_pd12s.rename(columns={"B01003_001E": "Population",
                                      "B01002_001E": "Median Age",
                                      "B19013_001E": "Household Income",
                                      "B23025_005E": "Unemployment Count",
                                      "B25058_001E": "Median Rent",
                                      "B25077_001E": "Median Home Value", 
                                      "NAME": "Name", 
                                      "state": "State"})
census_pd12s["Unemployment Rate"] = 100 *     census_pd12s["Unemployment Count"].astype(
        int) / census_pd12s["Population"].astype(int)
census_pd12s = census_pd12s[["Name", "State", "Population", "Median Age", "Household Income", "Unemployment Rate", "Median Rent", "Median Home Value"]]
census_pd12s["Year"] = "2012"


# amended 2013 code above
census_pd13s = pd.DataFrame(census_data13)
census_pd13s = census_pd13s.rename(columns={"B01003_001E": "Population",
                                      "B01002_001E": "Median Age",
                                      "B19013_001E": "Household Income",
                                      "B23025_005E": "Unemployment Count",
                                      "B25058_001E": "Median Rent",
                                      "B25077_001E": "Median Home Value", 
                                      "NAME": "Name", 
                                      "state": "State"})
census_pd13s["Unemployment Rate"] = 100 *     census_pd13s["Unemployment Count"].astype(
        int) / census_pd13s["Population"].astype(int)
census_pd13s = census_pd13s[["Name", "State", "Population", "Median Age", "Household Income", "Unemployment Rate", "Median Rent", "Median Home Value"]]
census_pd13s["Year"] = "2013"


# amended 2014 code above
census_pd14s = pd.DataFrame(census_data14)
census_pd14s = census_pd14s.rename(columns={"B01003_001E": "Population",
                                      "B01002_001E": "Median Age",
                                      "B19013_001E": "Household Income",
                                      "B23025_005E": "Unemployment Count",
                                      "B25058_001E": "Median Rent",
                                      "B25077_001E": "Median Home Value", 
                                      "NAME": "Name", 
                                      "state": "State"})
census_pd14s["Unemployment Rate"] = 100 *     census_pd14s["Unemployment Count"].astype(
        int) / census_pd14s["Population"].astype(int)
census_pd14s = census_pd14s[["Name", "State", "Population", "Median Age", "Household Income", "Unemployment Rate", "Median Rent", "Median Home Value"]]
census_pd14s["Year"] = "2014"


# amended 2015 code above
census_pd15s = pd.DataFrame(census_data15)
census_pd15s = census_pd15s.rename(columns={"B01003_001E": "Population",
                                      "B01002_001E": "Median Age",
                                      "B19013_001E": "Household Income",
                                      "B23025_005E": "Unemployment Count",
                                      "B25058_001E": "Median Rent",
                                      "B25077_001E": "Median Home Value", 
                                      "NAME": "Name", 
                                      "state": "State"})
census_pd15s["Unemployment Rate"] = 100 *     census_pd15s["Unemployment Count"].astype(
        int) / census_pd15s["Population"].astype(int)
census_pd15s = census_pd15s[["Name", "State", "Population", "Median Age", "Household Income", "Unemployment Rate", "Median Rent", "Median Home Value"]]
census_pd15s["Year"] = "2015"


#Append and drop for only 5 states

new = census_pd11s.append([census_pd12s,census_pd13s,census_pd14s,census_pd15s], ignore_index=True)
year5states = new.drop([0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 142, 143, 144, 146, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 194, 195, 196, 198, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 246, 247, 248, 249, 251, 253, 254, 255, 256, 257, 258, 259])
year5states

