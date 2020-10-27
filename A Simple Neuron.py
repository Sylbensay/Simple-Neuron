#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math


# In[5]:


# summation function
def sum_(input,weight):
    h = 0
    for x,w in zip(input,weight):
        h += x*w
        
    return h


# In[6]:


# hidden layer of the CNN contains the summation function and activation function
def hidden_layer(input,weight):
    
    #sum calculation
    sum_func = sum_(input,weight)
    
    #activation calculation (sigmoid function)
    output = 1/(1+math.exp(-sum_func))
    
    return output


# In[9]:


#Boolean function
def y_or_no(output):
    if output >= 0.5:
        return "Yes"
    if output < 0.5:
        return "No"


# In[10]:


input = [.5,.3,.2]
weight = [.4,.7,.2]
output = hidden_layer(input,weight)
print(y_or_no(output))


# In[ ]:




