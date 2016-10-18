
# coding: utf-8

# In[21]:

a=[1,2,3,4,4,4,4,5,5,5,5,6,7,8,9]


# In[22]:

def binary_search(x,y):
    low=0
    high=len(a)-1
    while (low<=high):
        mid=(low+high)/2
        if a[mid]==x:
            result=mid
            if(y):
                high=mid-1
            else:
                low=mid+1
        elif x>a[mid]:
            low=mid+1
        else:
            high=mid-1
    return result


# In[32]:

print("Occurence of 5 in the given array is ",1+binary_search(5,0)-binary_search(5,1))


# In[9]:

from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )


# In[10]:

for n in range(17):
    print ' '.join('%5d'%nCk(n,k) for k in range(n+1)).center(100)


# In[12]:

class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_next):
        self.next_node=new_next
        
    


# In[14]:

class LinkedList(object):
        def __init__(self,head=None):
            self.head=head
            
        def insert(self,data):
            new_node=Node(data)
            new_node.set_next(self.head)
            self.head=new_node
            
        def size(self):
            current=self.head
            count=0
            while current:
                count+=1
                current=current.get_next()
            return count
        
        def search(self,data):
            current=self.head
            found=False
            while current and found is False:
                if current.get_data()==data:
                    found=True
                else:
                    current=current.get_next()
            if current is None:
                raise ValueError("Data not in list")
            return current
        
        def delete(self,data):
            current=self.head
            previous-None
            found=false
            while current and found is False:
                if current.get_data()==data:
                    found=True
                else:
                    previous=current
                    current=current.get_next()
            if current is None:
                raise ValueError("Data not in list")
            if previous is None:
                self.head=current.get_next()
            else:
                previous.set_next(current.get_next())
            


# In[20]:

x=LinkedList()
x.insert(4)
x.insert(5)
x.insert(3)


# In[21]:

x.search(3)


# In[27]:

class stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


# In[28]:

S=stack()
for i in range(10):
    S.push(i)
    


# In[29]:

S.isEmpty()


# In[30]:

S.size()


# In[31]:

S.peek()


# In[32]:

class Queue(object):
    def __init__(self):
        self.list=[]
    def isEmpty(self):
        return self.list==[]
    def insert(self,data):
        self.list.insert(0,data)
    def dequeue(self):
        self.list.pop()
    def size(self):
        return len(self.list)


# In[33]:

Q=Queue()
for i in range(10):
    Q.insert(i)


# In[34]:

Q.isEmpty()


# In[35]:

Q.size()


# In[36]:

list


# In[37]:

Q.list


# In[38]:

Q.dequeue()


# In[39]:

Q.list


# In[46]:

a=[1,2,3,4,5,6]
for x in range(5):
    print '{0}, {1} ,{2}'.format(a[x % len(a)], a[(x+1) % len(a)],a[(x+2) % len(a)])


# In[51]:

for x in range(10):
        print a[x % len(a)],a[(x+1)%len(a)]


# In[66]:

class Node:
    def __init__(self,val):
        self.l_child=None
        self.r_child=None
        self.data=val
        
    def binary_inser(self,root,node):
        if root is None:
            root=node
        else:
            if root.data>node.data:
                if root.l_child is None:
                    root.l_child=node
                else:
                    binary_inser(root.r_child,node)
    
    def in_order_print(self,root):
        if not root:
            return
        in_order_print(root.l_child)
        print(root.data)
        in_order_print(root.r_child)
        
    def pre_order_print(self,root):
        if not root:
            return
        print root.data
        pre_order_print(root.l_child)
        pre_order_print(root.r_child)
    


# In[67]:

r=Node(3)
r.binary_inser(r,Node(7))
r.binary_inser(r,Node(1))
r.binary_inser(r,Node(5))


# In[68]:

r.in_order_print(r)


# In[73]:

#problem with end elements
A=[1,2,-10,3,2,-2]
def kadane_maximum_subarray():
    current_max=global_max=A[0]
    for i in range(1,len(A)-1):
        current_max=max(A[i],A[i]+current_max)
        if current_max > global_max:
            global_max=current_max
        
    return global_max
        


# In[74]:

kadane_maximum_subarray()


# In[1]:


def circular_kill():
    b=[]
    for i in range(1,100):
        b.append(i)
    if len(b)>1:
        del b[1::2]
    elif len(b)==1:
        print(b)


# In[1]:

import math
circular_kill_optimized(n):
    # n= no of players
    #square no to the power of 2 less than<n
    for i range(math.sqrt(n)):
        if(math.log2(i)<n):
            print(2*(100-)+1)
    


# In[3]:

import sys
def binary(n):
    if n>1:
        binary(n/2)
    print(int(n%2))
  
binary(9)


# In[97]:

binary(2)


# In[7]:

import math
n=math.log2(4)
n


# In[3]:

bin(int(4))


# In[1]:

from functools import reduce


# In[6]:

sum=reduce(lambda x,y:x+y,range(1,101))


# In[7]:

sum


# In[31]:

#for fibonacci
a=[0,1]
def fibo_generator(n):
    fibonacci=reduce(lambda x,y: a.append(a[-2]+a[-1]),range(n))
    print(a)


# In[32]:

fibo_generator(10)


# In[59]:

arr=[0,1]
def mod_fibo(n):
    reduce(lambda x,y: arr.append(arr[-2]+arr[-1]**2),range(n))
    print(int(arr[n-1]))


# In[62]:

mod_fibo(10)


# In[63]:

print(arr)


# In[65]:

temp=[int(j) for j in range(10)]


# In[66]:

temp


# In[84]:

import re
re.sub("[\W]",' ',"Hello India").split()


# In[82]:

str="This is ".split()
str


# In[139]:

replacement_array="Smartprix site india comparison best"
position_array="{} is {4} online {3} shopping {} in {}"
count=0
a=replacement_array.split()
def string_replace(str1):
    for i in range(len(str1)):
        if str1[i].isdigit():
            print(str1[i])
            for j in range(len(a)):
                print(str1[:i-1]+a[int(str1[i])]+str1[i+2:])
        #elif str1[i]=='{' and str1[i]=='}':
         #       count+=1
          #      print(str1[:i]+a[count]+str1[i+1:])
                
    print()

string_replace(position_array)



# In[173]:

a=[
[1,2,3],
[4,5,6],
[7,8,9]
]
def create_square_matrix(rows,columns):
    for i in range(rows):
        b=[]
        for j in range(columns):
            b.append(input("enter the element"))
        a.append(b)

def show_matrix(a,rows,columns):
    for i in range(rows):
        for j in range(columns):
            print(a[i][j])
        print("\n")
        
def matrix_multiplication(a,b,r1,r2,c1,c2):
    if r1!=c2:
        print("\nCannot multiply ")
    else:
        
    


# In[174]:

show_matrix(a,3,3)


# In[162]:

print(a[0][0])
print(a[1][1])
print(a[2][2])


# In[ ]:



