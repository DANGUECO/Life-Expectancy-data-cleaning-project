#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
get_ipython().run_line_magic('matplotlib', 'inline')


# LifeExpectancy.csv from the data201 course webpage, and read it into Python, skipping the necessary rows and reading the header. Make the country name be an index. Print the first few rows to ensure that you have it correct.

# In[2]:


# skipping the necessary rows and reading the header
life = pd.read_csv("C:/Users/dangu/OneDrive/Desktop/data201/LifeExpectancy.csv", skiprows=3, parse_dates=True)
# Make the country name be an index
l =life.set_index('Country Name', inplace=True)
display('Life Expectancy')
#  Print the first few rows
life.head()


# Drop rows that consist of NaN values. Be careful how you do this, the naive way of just using dropna() without looking at the data a bit might not do what you expect.
# You might need to know that to delete a column you can use `life.drop([list of column names],axis=1`.

# In[3]:


#drops all the columns
l = life.drop(['2018', '2019'],axis=1)
l = l.dropna(how = 'any')
l


# Now plot the curves of life expectancy against time on 1 plot for the following countries:  
# Afghanistan, Nepal, New Zealand, Netherlands
# Include a legend, and make the labels on the $x$-axis readable.

# In[4]:


#life expectancy vs time: Afghanistan, Nepal, New Zealand, Netherlands, legend, and make the labels on the  𝑥 -axis readable
afghan = life.iloc[1,5:-1]
afghan.plot(label = 'Afghanistan')

nepal = life.iloc[176,5:-1]
pl.plot(nepal, 'g', label = 'Nepal')

nz = life.iloc[178,5:-1]
pl.plot(nz, 'b', label = 'NZ')

nether = life.iloc[174,5:-1]
pl.plot(nether, color='yellow', label = 'Netherlands')

pl.xlabel('Time')
pl.ylabel('Life Expectancy(years)')

pl.legend()
pl.title('Life expectancy of Afghanistan, Nepal, New Zealand, Netherlands Line Graph(1960-2017)')


# Plot Rwanda separately, and explain briefly why it has that shape (hint: use wikipedia)

# In[5]:


rwanda = life.iloc[201,5:-1]
rwanda.plot( color='yellow')
pl.xlabel('Time')
pl.ylabel('Life Expectancy(years)')

pl.legend()
pl.title('Life expectancy of Rwanda Line Graph(1960-2017)')
#The cause is a genocide that occured around that time in rwanda around 1994. 
#It explains the huge dip as millions of people died during that period


# Can you detect any other countries where the life expectancy drops significantly? 
# 
# To compute this write some loops over each country and each year. If the next value is below 95% of the current value, print the name of the country. 

# In[6]:


#life = l.reset_index(drop=True)


# In[7]:


#inner loop is always completed first
#r starts as 0, then does all columns does all of c 0-finish
# drop the irrelevant countries
l = l.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
l


# In[8]:


#l.index.values is a reference point for the first loop, looping the rows as index values.
for r in l.index.values:
    #previous value has to be inside for loop.
    prevVal = 0
    for c in l:
        #inside loop works like [col][row] instead of [row][col]
        if prevVal-(prevVal/20) > l[c][r]:
            print(r)
            #break when if statement is found to avoid doubles.            
            break
            #else set the previous variable to be current one.
        else:
            prevVal = l[c][r]
            


# Compute the mean life expectancy for each of the countries over the whole 57 years. 
# Plot a bar chart of this for the first 10 countries. 

# In[9]:


#get columns 3 to 61 to get 1960-2017
#first 10 rows
# the mean for each 10 countries
l.iloc[0:10,3:61].mean(axis=1)


# In[10]:


#l is the new editted form
#l.columns
mean = l.iloc[0:10,3:61].mean(axis=1)
mean.plot.bar()
pl.xlabel('First 10 countries.')
pl.ylabel('Mean Life expectancy')
pl.title('Mean life expectancy for each of the countries over the whole 57 years ')


# Find the 5 countries with the highest mean life expectancy and the 5 with the lowest. You might find `life.sort_values()` helpful, as well as `pd.concat`and `life.transpose`. Plot a box and whisker plot of these countries. 

# In[11]:


l['mean'] = l.mean(numeric_only=True, axis = 1)
# l.sort_values() Sort by the values along either axis.
meanframe = l.sort_values(by='mean', ascending = False)


#Take the top 5
topfive = meanframe.head()
#Take the bottom 5
botfive = meanframe.tail()

#combine both new dataframes
combined = [topfive,botfive]
together = pd.concat(combined)
newframe = together.drop(['mean'], axis=1)

# life.transpose()Flips it diagonally.
# transpose the new dataframe
Nf = newframe.transpose()


#plot a box and whisker of all the countries.
boxplot = Nf.boxplot()
boxplot

