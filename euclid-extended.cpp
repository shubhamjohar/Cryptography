#include<iostream>
#include<math.h>
using namespace std;
int gcd_extended(int,int);
int main()
{
int a,b;
cout<<"\nEnter the value of a\n";
cin>>a;
cout<<"\nEnter the value of b\n";
cin>>b;
gcd_extended(a,b);
return 0;
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
cout<<"\n"<<x<<" "<<y<<" "<<d<<"\n ";
}  
