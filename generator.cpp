#include<iostream>
#include<math.h>
#include<stdbool.h>
bool is_prime(int);
int g_order();
int phi_function(int);
using namespace std;
int main()
{
cout<<phi_function(29)<<"\n";
cout<<phi_function(18)<<"\n";

return 0;
}
bool is_prime(int n)
{
int i,count=2;
int limit=sqrt(n);
for(i=2;i<=limit;i++)
 {
   if(n%i==0)
   { 
    count++;
   }
 }
if(count>2)
  {
    return false;
   }
else
   {
    return true;
   }
}


int gcd(int a,int b)
{
int remainder;
while(b!=0)
{
remainder=a%b;
if(remainder==0)
   {
   return b;
   } 
else
  {
  a=b;
  b=remainder;
  gcd(a,b);
  }
}
return b;
}


int g_order()
{
int n,k=1,a;
cout<<"\nEnter a value";
cin>>a;
cout<<"\nEnter value of n";
cin>>n;

while(int(pow(a,k)-1)%n!=0)
 {
   k++;
 }
return k;

}

int phi_function(int number)
{
if(is_prime(number))
{
  return number-1;
 }
else
{
  float result=1.0;
  int i,limit;
  limit=int(sqrt(number));
  for(i=2;i<limit;i++)
   {
     if((number%i==0) && is_prime(i))
      {
      result*=(1.0-float(1.0/float(i)));
      }
   }
if(number>1)
  result*=(1.0-float(1.0)/number);
return result*number;
}
}
