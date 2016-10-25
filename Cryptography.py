
# coding: utf-8

# In[1]:

from IPython.display import display, Math, Latex
import matplotlib.pyplot as plt


# <h1>Euclid Algorithm to find G.C.D.</h1>

# In[4]:

#Based on Euclid Algorithm
#a>=b
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a


# In[5]:

gcd(4,2)


# <h1>Binary Euclid Algorithm to find G.C.D.</h1>

# In[6]:

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
    
    
    


# In[7]:

binary_gcd(120,12)


# <h1>Extended Euclid Algorithm for solving Congruences</h1>

# In[8]:

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
        y2=y1
        y1=y
    d=a
    x=x2
    y=y2
    print(str(x)+" "+str(y))
    
        


# In[9]:

ext_euclid(4864,3458)


# <h1>Printing Prime Numbers in a given range</h1>

# In[10]:

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


# In[11]:

prime_numbers(5)


# In[12]:

#Based on Sieve of Eratosthenes
def prime_numbers(n):
    prime_array=[]
    sieve=[True]*(n+1)
    for i in range(2,int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i*2,n+1,i):
                sieve[j]=False
    for i in range(2,n+1):
        if sieve[i]:
            #print(i)
            prime_array.append(i)
    return prime_array

#Plotting of Primes
x=range(0,100000,25000)
size=len(x)
b=[]
for i in range(size):
   b.append(len(prime_numbers(x[i])))
#len(prime_numbers(100000))
plt.xlabel("Range")
plt.ylabel("No of Primes")
plt.plot(x,b,'b')


# In[13]:

B=[int(i) for i in range(10)]
B.remove(1)
B


# In[14]:

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


# In[16]:

check_prime(4523)


## Femrat's Primality Test

# In[ ]:

#k=number of times to test primality
def exp_mod(a,k,n):
    if a == 1:
        return 0
    c=1
    for i in range(1,k+1):
        c=(c*a)%n
    return c

def fermat_primality(number,k):
    if number>3:
        for i in range(k):
            a=random.randint(2,number-2)
            result=exp_mod(a,number-1,number)
            if result==1:
                fermat_primality(number,k-1)
            else:
                return 0
        
    elif number==2:
        print("\n 2 is even prime ")
        return 1
    elif number==0 or number==1:
        print("\n Invalid Input ")
        return 0
    
fermat_primality(97,15)
   


# <h1>Stirling's approximation</h1>

# In[9]:

def sterling_approx(n):
    t1=math.sqrt(2*math.pi)
    return t1*(n**((n+1)/2))*(math.e**(-n))
sterling_approx(100)
    


# <h1>Euclid Totient</h1>
# Number $n$ is written as $n=p_1^{k_1}p_2^{k_2}....p_i^{k_i}$ 
# 
# $\phi(n)=n(1-\frac{1}{p_1})(1-\frac{1}{p_2}).......(1-\frac{1}{p_i})$ where $p_i$ is a prime that divides $n$

# In[17]:

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

phi(100)

#N vs Phi(N) Graph
x=range(1,200)
y=[phi(x1) for x1 in x]
plt.xlabel("Numbers")
plt.ylabel("Phi(n)")
plt.plot(x,y,'bo',markersize=4)


# In[18]:

#Extended Euclid Algorithm for RSA
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
        q=int(math.floor(a/b))
        r=a-q*b
        x=x2-q*x1
        y=y2-q*y1
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    d=a
    x=x2
    y=y2
   # print(str(x)+" "+str(y))
    return x2


# <h1>Modular Exponentiation</h1>

# In[19]:

#Modulo Exponentiation
def exp_mod(a,k,n):
    if a == 1:
        return 0
    c=1
    for i in range(1,k+1):
        c=(c*a)%n
    return c


# <h1>R.S.A. Algorithm</h1>

# In[21]:

#RSA Algorithm
    
#print(check_prime(2357))
#print(check_prime(2551))

def calc_e(phi_value):
    found_e=1
    while found_e:
        e=random.randint(1,phi_value)
        if binary_gcd(e,phi_value)==1:
             found_e=0
    return e

def encrypt(phi_value,n):
    d_found=1
    while d_found:
       e=calc_e(phi_value)
       d=ext_euclid(e,phi_value)
       if d>0:
           d_found=0
    print("Secret Key of A is",d)
    print("E value is",e)
    #MESSAGE
    message=5234673
    #Or  message=input()
    print("Message is",message)
    cipher_text=exp_mod(message,e,n)
    
    #Display Cipher Text 
    print("Cipher Text is ",cipher_text)
    return str(cipher_text)+" "+str(d)

def  decrypt(cipher_text,d,n):
    return exp_mod(cipher_text,d,n)

def RSA(p,q):
    n=p*q
    phi_value=(p-1)*(q-1)
    #Encryption by B
    cipher_text,d=encrypt(phi_value,n).split(' ')
    cipher_text,d=[int(cipher_text),int(d)]
    #Decryption  by A
    message_decrypt=exp_mod(cipher_text,d,n)
   
    print("Decypted message is",decrypt(cipher_text,d,n))


# In[22]:

RSA(2357,2551)


# <h1>DES</h1>
# <img src="https://www.tutorialspoint.com/cryptography/images/des_structure.jpg">

### One-time pad

# In[7]:

def convert_to_bits(n,padding):
    result=[]
    while n>0:
        if n%2==0:
            result=[0]+result
        else:
            result=[1]+result
        n=int(n/2)
    while len(result)<padding:
        result=[0]+result
    return result


# In[9]:

convert_to_bits(1,5)


# In[37]:

def string_to_bits(message):
    result=[]
    for i in range(len(message)):
        result.append(convert_to_bits(ord(message[i]),7))
    return result


# In[38]:

print(string_to_bits("SHUBHAM"))


# In[20]:

#Mainly for Binary Numbers(Not Modified)
def XOR(x,y):
    if x==y:
        return 0
    else:
        return 1


# In[21]:

XOR(1,0)


# A positive integer $n$ has $b$ bits when $2^{b-1} \leq n \leq 2^{b} – 1$

# In[29]:

import math
floor(log2(49)+1)


## Miller-Rabin Test

# In[25]:

def miller_rabin(n,t):
    for i in range(1,t):
        s,r=find_sr(n-1).split(' ')
        a=random.randint(2,(n-2)+1)
        y=exp_mod(a,r,n)
        if y!=1 and y!=n-1:
            j=1
            while j<=s-1 and y!=n-1:
                y=y**2%n
                if y==1:
                    return 0
                    j+=1
            if y!=n-1:
                return 0
    return 1
    #return "{0:b}".format(n-1)

def  find_sr(n):
    return str(3)+" "+str(5)

def exp_mod(a,k,n):
    if a == 1:
        return 0
    c=1
    for i in range(1,k+1):
        c=(c*a)%n
    return c

miller_rabin(91,1)
    


## Elgmal Algorithm

# ElGamal encryption consists of three components: 
# <ol>
# <li><strong>the key generator</strong></li>
# The key generator works as follows:
# <ul>
#         <li>Alice generates an efficient description of a cyclic group $G$,of order $q$, with generator $g$.</li>
#         <li>Alice chooses an $x$ randomly from ${1,.....q-1}$.</li>
#         <li>Alice computes $h:=g^{x}$.</li>
#         <li>Alice publishes $h$, along with the description of $G,q,g$ as her public key. Alice retains $x$ x as her private key, which must be kept secret</li>
# </ul>
# <li>the encryption algorithm</li> 
# <li>and the decryption algorithm</li>
# <ol>

# In[ ]:



