#include<iostream>
int gcd(int,int);
int main()
{
int a,b;
std::cout<<"\nEnter the coeffiicients of a and b\n";
std::cin>>a>>b;
std::cout<<"\nGCD of "<<a<<" and "<<b<<" is:"<<gcd(a,b);
return 0;
}
int gcd(int a,int b)
{
int g;
if(a==b)
{
  return a;            //or b
}

if(a==0)
{
 return b;
}

if(b==0)
{
 return a;
}

if(!(a & 1))                //a is even
  {
  if(!(b & 1))
   {
	return (2*gcd(a>>1,b>>1));         // a and b are even
   }
   else
   {
     return gcd(a>>1,b);                  // a is even and b is  odd
   }
 } 

if((a & 1) && (b & 1))
 {
    if(a>=b)
     {
     return gcd((a-b)/2,b);
     }
     else
     {
     return gcd((b-a)/2,a);
     }	
 }
}


