
# coding: utf-8

## Shamir's Secret Sharing Scheme

# <strong>Shamir's Secret Sharing </strong> is an algorithm in cryptography created by Adi Shamir.It is a form of secret sharing,where a secret is divided into parts giving each participant its own unique part,where some of the parts or all of them are needed in order to reconstruct the secret.
# 
# Counting on all participants to combine the secret might be impractical and therefore sometimes the threshold scheme is used where any k f the parts are sufficient to reconstruct the original secret.

# The goal is to divide secret $S$ into $n$ pieces of data $S_1,S_2,...S_n$ in such a way that:
# <ol>
# <li>knowledge of any $k$ or more $S_i$ pieces makes $S$ easily computable</li>
# <li>Knowledge of any$k-1$ or fewer $S_i$ pieces leaves $S$ completely undetermined
# </ol>
# 
# This scheme is called $(k,n)$ threshold scheme.If $k=n$ then all participants are required to reconstruct the secret.
# 
# To divide it into pieces,we pick a random $t-1$ degree polynomial
#  $q(x)=a_0+a_1x+a_2x^2+........+a_{t-1}x^{t-1}$

#### Example

# Suppose that our secret is 1234$(S=1234)$.
# 
# We wish to divide the secret into 6 parts$(n=6)$ where any subset of 3 part$(k=3)$ is sufficient to reconstruct the secret.At random we obtain two $(k-1)$ numbers:$166$ and $94$.
# 
# $(a_0=1234;a_1=166;a_2=94)$
# 
# Our polynomial to produce secret shares(points) is therfore:
# $q(x)=1234+166x+94x^2$
# 
# We create  points $D_1=q(1),....D_i=q(i),...D_n=q(n)$
# 

#### Lagranges Polynomial Interpolation 

# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Lagrange_polynomial.svg/440px-Lagrange_polynomial.svg.png">
# This image shows, for four points ((−9, 5), (−4, 2), (−1, −2), (7, 9)), the (cubic) interpolation polynomial L(x) (dashed, black), which is the sum of the scaled basis polynomials y0ℓ0(x), y1ℓ1(x), y2ℓ2(x) and y3ℓ3(x). The interpolation polynomial passes through all four control points, and each scaled basis polynomial passes through its respective control point and is 0 where x corresponds to the other three control points.

# $L(x)=\sum_{j=0}^{t}y_jl_j(x)$ 
# 
# where $l_j(x)=\prod_{0 \leq m<2, m \neq j}(\frac{x-x_m}{x_j-x_m})$

### Algorithm/Scheme Implementation:

# In[1]:

import random
import math


# In[5]:

#Calculating D

n=int(input("Enter the number of locks "))
k=int(input("Enter the keys required "))

arr=[]

secret_key=int(input("Enter the secret key "))
arr.append(secret_key)
nc=int(input("Enter the no of coefficients "))
#Input coefficients
for i in range(nc):
    arr.append(int(input("Enter the "+str(i+1)+" coefficient ")))
    
print "\n Function coefficients are(First element is the secret) ",arr
  
def eval_poly(x,a):
    result=0
    for i in range(len(a)):
        result+=a[i]*x**i
    return result  

D_arr=[]
def D_array():
    #D_arr=[]
    for i in range(1,n+1):
        temp=[]
        for j in range(1):
            temp.append(i)
            temp.append(eval_poly(i,arr))
        D_arr.append(temp)
    return D_arr

print "\nD Array is ",D_array()

#Finding l(x)

#Randomly taking any 3 keys
    
x_arr=[1,3,4]

#kn=int(input("enter the number of shares"))
#x_arr=[]
#for i in range(kn):
#    x_arr.append(int(input()))

print "\n Taking  any  random keys pair",x_arr

l_array=[]

def l_x(t):
    result_numerator=1
    result_denominator=1
    for i in range(t):
        temp=[]
        for j in range(1,t):
            result_numerator=poly_mult([-1,x_arr[(i+1)%t]],[-1,x_arr[(i+2)%t]])
            result_denominator=(x_arr[i%t]-x_arr[(i+1)%t])*(x_arr[i%t]-x_arr[(i+2)%t])
        temp.append(result_numerator)
        temp.append(result_denominator)
        l_array.append(temp)
    return l_array
        
def poly_mult(p,q):
    result_prod=[0]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            result_prod[i+j]+=p[i]*q[j]
    return result_prod

print "\n First array is for coefficients of numerator and second is for denominator ",l_x(3)

def poly_add(p,q):
    result_sum=p
    for i in range(len(q)):
        result_sum[i]+=q[i]
    return result_sum

def Lagranges_Interpolation():
    L_array=[1]*len(x_arr)
    L=[]
    #L_arrays store y0 divided by l(x) denominator
    for i in range(len(x_arr)):
        L_array[i]=(D_arr[x_arr[i]-1][1])/l_array[i][1]
    for i in range(len(L_array)):
        t=[]
        temp=l_array[i][0]
        for j in range(len(temp)):
            t.append(temp[j]*L_array[i])
        L.append(t)
    return reduce((lambda x,y:poly_add(x,y)),L)

coefficients=Lagranges_Interpolation()
#Decoded
print "\n Coefficients are ",coefficients,"(decreasing power of x) "
    


# In[ ]:

D_arr=[[1, 6], [2, 13], [3, 24], [4, 39]]
x_arr=[1, 3, 4] 
l_array=[[[1, -7, 12], 6], [[1, -5, 4], -2], [[1, -4, 3], 3]]
L_array=[1]*3


# In[ ]:

for i in range(len(x_arr)):
    L_array[i]=(D_arr[x_arr[i]-1][1])/l_array[i][1]


# In[37]:

L_array


# In[14]:

test1= [[1, -7, 12],[1, -5, 4],[1, -4, 3]]
def test():
    return reduce(lambda x,y:x*y,range(1,10))

def poly_mult(test):
    result_prod=[0]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            result_prod[i+j]+=p[i]*q[j]
    return result_prod
test()


# In[27]:




# In[ ]:



