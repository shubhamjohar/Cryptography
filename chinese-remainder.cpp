#include<iostream>
#include<math.h>
int sieve_eratosthenes(int);
int main()
{
int n,i;
std::cout<<"\nEnter the range";
std::cin>>n;
sieve_eratosthenes(n);

return 0;
}
int sieve_eratosthenes(int n)
{
std::cout<<"\nSize received is"<<n<<"\n";
int size=n;
int array[n];
int p=sqrt(n);

std::cout<<"pow 1/2 is"<<p<<"\n";
for(int i=2;i<p;i++)
{
    if(array[i]!=0)
   { for(int j=2*i;j<=n;j+=i)
     array[j]=0;
   } 
}
//printing
for(int i=0;i<n;i++)
{
  if(array[i])
  std::cout<<i<<" ";
}
return 0;
}
