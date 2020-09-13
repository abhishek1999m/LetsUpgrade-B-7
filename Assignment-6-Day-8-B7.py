#!/usr/bin/env python
# coding: utf-8

# # Q1.

# In[12]:


def value(x):
    def fibnum(y):
        return(x(y))
    return fibnum

@value
def fibonacci(n):
    a=0
    b=1
    sum=0
    count=1
    print("Fibonacci series",end=',')
    while count<=n:
        print(sum,end=",")
        count+=1
        a=b
        b=sum
        sum=a+b


# In[14]:


fibonacci(14)


# In[15]:



import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
    text = fh.readlines()
    fh.close()
except IOError:
    print('cannot open', file_name)

if text:
    print(text[100])

