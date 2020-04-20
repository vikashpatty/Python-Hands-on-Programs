#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/python
a, b = 20, 10
c = a + b
print('\n Addition of two numbers is', c)
c = a - b
print('\n Subtraction of two numbers is', c)
c = a * b 
print('\n Multiplication of two numbers is', c)
c = a / b 
print('\n Division of two numbers is', c)


# In[6]:


#!/usr/bin/python
a, b, c = 20, 10, 30
if a > b and a > c:
    print('Biggest of three numbers is', a)
if b > a and b> c:
    print('Biggest of three numbers is', b)
if c > a and c > b:
    print('Biggest of three numbers is', c)


# In[7]:


#!/usr/bin/python
a = 10
b = a % 2
if b == 0 :
    print('Given number is', c,'even')
else:
    print('Given number is', c,'odd')


# In[10]:


#!usr/bin/python
a = 7
for i in range(1, a-1):
    if a % i == 0 :
        print('The given number', a,'is not prime')
    else:
        print('The given number', a,'is prime')
        break


# In[12]:


#!/usr/bin/python
#to pass command line ARG you need to create a .py file for below code and pass arg
import sys
#comment below three line if passing arg from cmd, i'm using jupter so taking as input to show output
arg1=int(input('Enter 1st arg:'))
arg2=int(input('Enter 2nd arg:'))
arg3=int(input('Enter 3rd arg:'))
print('First number is', arg1)
print('Second number is', arg2)
print('Third number is', arg3)
print ('The biggest of three numbers is', max(arg1, arg2, arg3))


# In[14]:


#!usr/bin/python
str1 ='Chennai'
str2 = 'City'
for i in str1:
    print('current letter is', i)
str3 = str1[2:5]
print ('Sub string is', str3)
print ('Repeated string is ', str1 * 5)
print ('Concatenated string is ', str1 + str2)


# In[16]:


#!/usr/bin/python
List1 = [12, 23, 'Hello', 60.6, 'Chennai']
List2 = [21, 32, 60]
a = List1 [1:3] 
b = List1 * 2
c = List1 + List2
print('\n', a )
print('\n', b )
print('\n', c )


# In[17]:


#!/usr/bin/python
Tuple1 = (12, 23, 'Hello', 60.6, 'Chennai')
Tuple2 = (21, 32, 60)
a = Tuple1[1:3] 
b = Tuple1 * 2
c = Tuple1 + Tuple2
print('\n', a )
print('\n', b )
print('\n', c )


# In[22]:


#!/usr/bin/python
a = complex(input('Enter 1st input in form of a + bj:'))
b = complex(input('Enter 2nd input in form of a + bj:'))
c = a + b
print ('\n Addition of two numbers is', c)
c = a - b
print ('\n Subtraction of two numbers is', c)
c = a * b 
print ('\n Multiplication of two numbers is', c)
c = a / b 
print ('\n Division of two numbers is', c)


# In[23]:


#!/usr/bin/python
a=int(input('Enter Number:'))
b=1
b += a
print('\n Addition of two numbers is', b)
b -= a
print('\n Subtraction of two numbers is', b)
b *= a 
print('\n Multiplication of two numbers is', b)
b /= a 
print('\n Division of two numbers is', b)
b %= a
print('\n modulus of two numbers is', b)
b **= a
print('\n Exponentiation of two numbers is', b)
b //= a
print('\n Floor division of two numbers is', b)


# In[26]:


#!/usr/bin/python
a=int(input('Enter 1st Number:'))
b=int(input('Enter 2nd Number:'))
c = a and b
d = a or b
e = not(a and b)
print(a)
print(b)
print(c)
type(c)


# In[ ]:




