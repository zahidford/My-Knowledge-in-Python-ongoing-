#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


# SIMPLE MATHEMATICS 


# In[5]:


var = 7**(4)


# In[6]:


var


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[4]:


# Splitting of string


# In[9]:


S='hi there Sam'


# In[11]:


S


# In[12]:


S.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[18]:


planet = "Earth"
diameter = 12742


# In[19]:


print ('The diameter of {} is {} kilomenters' .format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[20]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[21]:


lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[23]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[28]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[30]:


# Tuple is immutable but list is mutable


# In[ ]:


# best answer in this location https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[58]:


def returndomain (var):
    x= (var.split("@")[1])
    print ('the domain name is {}'.format(x))
    print (var.split("@")[1])
#print ('domain name is {}'.format(dark))


# In[59]:


returndomain('zahidford@domain.com')


# In[60]:


returndomain('zahidford@bogus.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[66]:


def checkdog (var):
    if 'dog' in var:
        print ('TRUE')


# In[67]:


checkdog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[72]:


def countdog (var):
    numberofdog= var.count('dog')
    print (numberofdog)
    


# In[73]:


countdog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[84]:


seq = ['soup','dog','salad','cat','great']


# In[78]:


seq2 =[1,2,3,4,5,6,7,8]


# In[88]:


list(filter(lambda word: word[0]=='s', seq))


# In[ ]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[105]:


def caught_speeding(speed, is_birthday):
    if is_birthday :
        speeding = speed -5
    else:
        speeding = speed
    if speeding >80:
        print('BIG TICKET')
    elif speeding >60 :
        print('Small Ticket')
    else:
        print('No Ticket')


# In[106]:


caught_speeding(81,True)


# In[107]:


caught_speeding(81,False)


# # Great job!
