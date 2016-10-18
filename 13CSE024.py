import random
import math

def check_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count>2:
        return 0      #Not Prime
    else:
        return 1      #Prime

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
    
def exp_mod(a,k,n):
	if a == 1:
		return 0
	c=1
	for i in range(1,k+1):
		c=(c*a)%n
	return c

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
  



            
  
RSA(2357,2551)
