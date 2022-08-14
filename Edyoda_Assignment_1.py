#!/usr/bin/env python
# coding: utf-8

# In[85]:


a=0           #int(input("First number : "))
e=1           #int(input("Second number :"))
d=50          #int(input("End of Range :"))
b=a+e         #1
while b<d:
        c=a+b #---C=1,2,3,5,8,13,21,34,55
        a=b   #---a=1,1,2,3,5,8,13,21,34
        b=c   #---b=1,2,3,5,8,13,21,34,55
        print(a)


# In[86]:


a=input("Enter the word: ")
b=len(a)
i=1
x=""
while i<=b:
    x=x+a[b-i]
    i=i+1
print(x)
print(b)


# In[88]:


print("Enter the starting and ending of numbers series")
a=int(input("Start : "))
b=int(input("End : "))+1
x=range(a,b)
print(list(x))
y=len(x)
print("Total Numbers : ",y)
i=0
ce=0
co=0
while i<y :
    p=x[i]%2
    if p==0:
        ce=ce+1
    else:
        co=co+1
    i=i+1
print("Even Numbers :",ce)
print("Odd Numbers :",co)


# In[ ]:





# In[ ]:




