#!/usr/bin/env python
# coding: utf-8

# Q1

# In[13]:


class Bank_Account:
    def __init__(self,ownerName,Balance):
        self.ownerName=ownerName
        self.Balance=Balance
    def deposite(self):
        name=input("Enter the name of account owner: ")
        if name==self.ownerName:
            a=int(input("Enter Amount to be deposite in the bank account: "))
            self.Balance=self.Balance+a
            print(" Now Available Balance in the account: ",self.Balance)
        else:
            print("Invalid! User name!")
    def withdrwal(self):
        name=input("Enter the name of account owner: ")
        if name==self.ownerName:
            a=int(input("Enter Amount to be deposite in the bank account: "))
            if a<=self.Balance:
                self.Balance=self.Balance-a
                print(" Now Avauilable balance after withdrwal: ",self.Balance)
            else:
                print("Insufficient Fund, Please enter Valid amount for Withdrwal")
        else:
            print("No, Such USer is found in the bank record!")


# In[14]:


A=Bank_Account('Abhi',500)


# In[15]:


A.withdrwal()


# In[16]:


A.deposite()


# Q.2.
# 

# In[17]:


import math
class cone:
    
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def volume(self):
        volume=(1.0/3) * math.pi * self.radius * self.radius * self.height
        print("Volume of the cone is: ",volume)
        
    def surface_Area(self):
        s = math.pi*math.sqrt(self.radius * self.radius + self.height * self.height)
        b = math.pi*self.radius*self.radius
        SA=s+b
        print("Surface area of the cone is: ",SA)


# In[23]:


Cone=cone(float(input("Enter Radius: ")),float(input("Enter height: ")))


# In[24]:


Cone.volume()


# In[25]:


Cone.surface_Area()

