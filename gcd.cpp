
#include<iostream>
using namespace std;
int gcd(int,int);
int main()
{
int a,b;
cout<<"\nEnter the value of a\n";
cin>>a;
cout<<"\nEnter the value of b\n";
cin>>b;
cout<<"\nGCD of "<<a<<" and "<<b<<" is :  "<<gcd(a,b)<<"\n";
return 0;
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
