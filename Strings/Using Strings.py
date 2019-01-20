#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Using Strings


# In[2]:


# we can represnt is by Single Quotes or double Quotes


# In[3]:


'hello'


# In[4]:


"hello"


# In[5]:


# we can grab Characters


# In[6]:


# We can also "slice" a string [star:stop:step]


# In[7]:


'this is also a string'


# In[8]:


'I am going on a run'


# In[10]:


print("hello")
print("hello2")


# In[11]:


#Using Escape Sequence \n


# In[12]:


print('hello \n world')


# In[13]:


# length of a string
len('hello')


# In[14]:


len ('i am')


# In[16]:


print ("HELLO WORLD")


# In[17]:


#indexing and Slicing


# In[18]:


my_string= "Hello World"


# In[19]:


my_string[0]


# In[20]:


my_string[8]


# In[21]:


my_string[-2]


# In[22]:


#slicing


# In[24]:


mystring= 'abcdefghijklmnopqrstuvwxyz'


# In[26]:


mystring[2:]


# In[27]:


mystring[:4]


# In[28]:


mystring[3:6]


# In[29]:


mystring[1:3]


# In[30]:


mystring[::]


# In[31]:


#jumping


# In[32]:


mystring[::4]


# In[33]:


# From and notinclucding and Step Jumping


# In[36]:


mystring[2:7:2]


# In[39]:


mystring[::-1]


# In[40]:


# sTRING properties and methods


# In[41]:


# String is immutable once declated you cannot change it
name ='sam' #nsme[0]= 'p' is not possiblr


# In[42]:


# But we can Concatenet it


# In[43]:


last_letters = name[1:]


# In[44]:


last_letters


# In[46]:


'p'+last_letters


# In[47]:


# Another example


# In[48]:


X='hello world'


# In[49]:


X=X + "it is beautiful outside"


# In[50]:


X


# In[51]:


#LETTER INCREMENT


# In[52]:


LETTER = 'Z'


# In[53]:


LETTER *10


# In[54]:


2+3


# In[55]:


'2'+'3'


# In[57]:


# not allowed '2'+3


# In[58]:


# Built in methods


# In[59]:


x = 'hello world'


# In[60]:


# type x.tab


# In[61]:


x.upper


# In[62]:


x


# In[63]:


x.upper()


# In[65]:


x.lower()


# In[66]:


x.split()


# In[68]:


x.split('o')


# In[69]:


# String Formtting and Printing


# In[70]:


print('this is a string {}'.format('Inserted'))


# In[71]:


print('The {} {} {}'.format('fox','brown','fox'))


# In[72]:


print('The {2} {2} {2}'.format('fox','brown','fox'))


# In[74]:


print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))


# In[ ]:




