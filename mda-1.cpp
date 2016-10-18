#include<iostream>
#include<math.h>
void straight_method(long,long,long);
int main()
{
long   a,k,n;
std::cout<<"\nEnter value of a\nk\n and n";
std::cin>>a>>k>>n;
straight_method(a,k,n);
return 0;
}
void straight_method(long a,long n,long k)
{

long power=pow(a,k);
std::cout<<"\n a^k mod n is\n"<<power%n;

}
