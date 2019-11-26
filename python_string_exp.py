#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python string examples.
singlequote = 'sambasivarao'

doublequote = "Tammavarapu"

triplequote = """nawabupet,ndg(bo)
                 krishna,Ap-521185"""


# In[2]:


# Strng slicing
print(singlequote[:])                
print(doublequote[:])
print(triplequote[:])


# In[3]:


# new strings can be reassigned to the same name
name = 'samba'
name = 'sambasivarao'

print(name)


# In[4]:


# Con't deleate and update a string but use build-in function del to remove string.
str_name=''
del str_name


# In[5]:


# Formatting of Strings
"{} {} {}".format('Geeks', 'For', 'Life')
"{1} {0} {2}".format('Geeks', 'For', 'Life')
"{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life')
"{0:b}".format(16) # Formatting of Integers
"{0:e}".format(165.6458) # Formatting of Floating
"{0:.2f}".format(1/6) #  Rounding off Integers 


# In[6]:


# String methods examples
str = "Python Machine Learning"

print('***********String upper case examples*****************')
# uppercase
print("string is uppercase   : ",str.isupper())
print("string into uppercase : ",str.upper())
upper = str.upper()
print("string in uppercase   : ",upper.isupper())
print()
print('***********String lowser case exp*********************')
# uppercase
print("String is lowercase   : ",str.islower())
print("string into lowercase : ",str.lower())
lower = str.lower()
print("string in lowercase   : ",lower.islower())
print('******************************************************')


# In[8]:


name = 'samba'
empid = 'TS538345'
sal = '25000'

print("Emp Name is alpha :",name.isalpha())
print("Emp Name is alpha numeric :",name.isalnum())
print("Emp sal is decimal :",sal.isdecimal())
# str.space()
# str.title()
# str.startswith('python')
# str.endswith('learning')
# str.find('Python')
# str.strip()
# str.lstrip()
# str.rstrip()
# str.center()
# str.ljust()
# str.rjust()
# str.index('p') 
# str.split()
# str.replace('Machine','AI')
# len(str)
# print(''.join(reversed(name)))
# str1.join(str2)
# str.count()
print('******************************************************')


# In[ ]:




