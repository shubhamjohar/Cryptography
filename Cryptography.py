
# coding: utf-8

# In[30]:

from IPython.display import display, Math, Latex
import matplotlib.pyplot as plt


# In[31]:

#Based on Euclid Algorithm
#a>=b
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a


# In[32]:

gcd(4,2)


# In[33]:

#Binary Euclidean Algorithm
def binary_gcd(a,b):
    if a==b:
        return a
    if a==0:
        return b
    if b==0:
        return a
    if a & 1==0:       #a is even
        if b & 1:
            return binary_gcd(a>>1,b)
        else:
            return binary_gcd(a>>1,b>>1)<<1
    if a & 1:         #a is odd
        if b & 1==0:  #b is even
            return binary_gcd(a,b>>1)
        else:
            if a>=b:
                return binary_gcd((a-b)>>1,b)
            else:
                return binary_gcd((b-1)>>1,a)
    
    
    


# In[34]:

binary_gcd(120,12)


# In[13]:

#Extended Euclidean Algorithm

def ext_euclid(a,b):
    if b==0:
        d=a
        x=1
        y=0
        print(str(x)+" "+str(y))
    x2=1
    x1=0
    y2=0
    y1=1
    while b>0:
        q=a//b
        r=a-q*b
        x=x2-q*x1
        y=y2-q*y1
        a=b
        b=r
        x2=x1
        x1=x
        y2=1
        y1=y
    d=a
    x=x2
    y=y2
    print(str(x)+" "+str(y))
    
        


# In[14]:

ext_euclid(4864,3458)


# In[15]:

#Based on Sieve of Eratosthenes
def prime_numbers(n):
    sieve = [True] * (n + 1)  # create a list n elements long
    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    for i in range(2, n + 1):
        if sieve[i]:
            print(i)
            
    
    


# In[16]:

prime_numbers(5)


# In[17]:

B=[int(i) for i in range(10)]
B.remove(1)
B


# In[18]:

#brute force check for primality
def check_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 0                #Not Prime
    else:
        return 1                #Prime


# In[19]:

check_prime(4523)


# In[20]:

# phi(n) calculates the numbers less than n that are relatively prime with 'n'
def check_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 0                #Not Prime
    else:
        return 1                #Prime
    
def phi(n):
    result=n
    #for prime numbers phi(n)=n-1
    if check_prime(n):
        return n-1
    else:
        for i in range(2,n):
            if n%i==0 and check_prime(i):
                result*=(1.0-float((1.0/float(i))))
           # print(result)
    return int(result)
    


# In[21]:

phi(100)


# In[ ]:




# In[ ]:




# In[42]:




# In[42]:




# In[42]:




# In[42]:




# In[42]:




# In[ ]:



