#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
string = 'aaa--bbb==ccc__ddd'
re.split(r'--|==|__', string)


# In[3]:


string = 'Yesterday, All my troubles seemed so far away'
pattern = re.compile(r'^[a-zA-Z]+\b')
pattern.match(string).group()


# In[4]:


pattern = re.compile(r'[a-zA-Z]+$')
pattern.search(string).group()


# In[11]:


s= '''My uncle -- high ideals inspire him;
but when past joking he fell sick,
he really forced one to admire him --
and never played a shrewder trick.
Let others learn from his example!
But God, how deadly dull to sample
sickroom attendance night and day
and never stir a foot away!'''
a = re.findall(r'\by\w*\b',s)
b = re.findall(r'\bi\w*\b',s)
c = re.findall(r'\bu\w*\b',s)
d = re.findall(r'\ba\w*\b',s)
e = re.findall(r'\be\w*\b',s)
f = re.findall(r'\bo\w*\b',s)
print (a,d,c,d,e,f)


# In[9]:


a = re.findall(r'^\w+',s,re.M)
print (a)


# In[16]:


a = str(input())
b = re.compile(r'[^\s@]+[@][\w]+[.][\w]+')
if b.match(a):
    print ('correct')
else:
    print ('incorrect')


# In[18]:


a = ('1234@gmail.com,1234@mail.ru,1234@yandex.ru,1234,ru')
b = re.compile(r'[@][\w]+[.]')
c = re.findall(b,a)
print([i[1:-1] for i in c])


# In[ ]:





# In[33]:


a = str(input()) 
if re.match(r'[+7][0-9]{11}', a) or re.match(r'[+7]*[\(]([0-9]{3})*[\)][0-9]{3}(?:-\d{2}){2}', a) or re.match(r'[+7]*(?:\s\d{2,3}){4}', a) or re.match(r'[+7]+[\s][\(]([0-9]{3})[\)]+[\s][0-9]{3}(?:-\d{2}){2}', a) or re.match(r'[+7]*[\s]([0-9]{3})*[\s][0-9]{3}(?:-\d{2}){2}', a):
    print(a, 'correct')
else:
    print(a, 'incorrect')

