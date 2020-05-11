#!/usr/bin/env python
# coding: utf-8

# In[118]:


import pandas as pd
from matplotlib import pyplot as ptp
df=pd.read_csv("ex1data1.txt")
x=df.iloc[0:,0]


# In[119]:


ptp.style.use('fivethirtyeight')


# In[120]:


y=df.iloc[0:,1]


# In[121]:


x


# In[122]:


y


# In[123]:


ptp.xlabel('Population of City in 10,000s')
ptp.ylabel('Profit in $10,000s')
ptp.title('Scatter plot of training data')
ptp.scatter(x,y,edgecolors='black')


# In[124]:


def gradient_descent(x,y):
    theta_one=theta_not=0
    iterations=1500
    learning_rate=0.01
    n=len(x)
    for i in range(iterations):
        y_predicted=theta_one*x+theta_not
        theta_oned=(1/n)*sum((y_predicted-y)*x)
        theta_notd=(1/n)*sum(y_predicted-y)
        theta_one=theta_one-learning_rate*theta_oned
        theta_not=theta_not-learning_rate*theta_notd
    print(theta_one)
    print(theta_not)
    ptp.xlabel('Population of City in 10,000s')
    ptp.ylabel('Profit in $10,000s')
    ptp.title('Scatter plot of training data')
    ptp.scatter(x,y,edgecolor='black')
    
    ptp.plot(x,y_predicted,color='red')
gradient_descent(x,y)

        


# In[ ]:





# In[ ]:





# In[ ]:




