#include<iostream>
#include<math.h>
int  square_method(int,int,int);
void binary(int);
int main()
{
int a,k,n;
binary(100);
std::cout<<"\nEnter value of a\nk\n and n";
std::cin>>a>>k>>n;
square_method(a,k,n);
return 0;
}

void binary(int  n)
{
    int decimalNumber = 0, i = 0, remainder;
    while (n!=0)
    {
        remainder = n%10;
        n /= 10;
        decimalNumber += remainder*pow(2,i);
        ++i;
    }
    cout<< decimalNumber;
}
int  square_method(int a,int n,int k)
{
int power;
int b=1;
if(k==0)
 {
  return b;
 }
long AA=a;
std::cout<<"\n a^k mod n is\n"<<power%n;

}
~                                                                               
~      
