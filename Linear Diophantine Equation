#include<iostream>
#include<math.h>
int gcd(int,int);
int gcd_extended(int,int);
using namespace std;
int t;
int main()
{
int x,y,c;
cout<<"\nEnter the  coefficients of x and y and c value  respectively";
cin>>x>>y>>c;
int gcd_xy=gcd(x,y);
cout<<"\nGCD of "<<x<<" and "<<y<<" is "<<gcd_xy;
if(gcd_xy)
  {
   if((c%gcd_xy)==0)
    {
     ::t=c/gcd_xy; 
     cout<<"\nSolution Exists\n";
     gcd_extended(x,y);
    }
    else
    {
     cout<<"\nSolution doesn't exist\n";
    }
  }
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



int gcd_extended(int a,int b)
{
int d,x,y,r,q;                     //d=gcd(a,b)
if(b==0)
  {
  d=a;
  x=1;
  y=0;
  cout<<"\n d= "<<d<<" x= "<<x<<" y= "<<y<<"\n";
  }
int x2,x1,y2,y1;
x2=1;
x1=0;
y2=0;
y1=1;
  while(b>0)
  {
  q=floor(a/b);
  r=a-q*b;
  x=x2-q*x1;
  y=y2-q*y1;
  a=b;
  b=r;
  x2=x1;
  x1=x;
  y2=y1;
  y1=y;
  }
d=a;
x=x2;
y=y2;
cout<<"\n x0 is "<<x<<"\n y0 is "<<y<<"\n and  d= "<<d<<"\n ";

cout<<"\n x is "<<x*t<<"\n y is "<<y*t<<" \n";

}
      
