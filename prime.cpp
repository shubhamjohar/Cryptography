#include <bits/stdc++.h>
#include<fstream>
using namespace std;
 
void SieveOfEratosthenes(int n)
{ 
   ofstream write;
   write.open("data.txt",std::ios_base::app);
   int count=0;
    bool prime[n+1];
    memset(prime, true, sizeof(prime));
 
    for (int p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
 
    for (int p=2; p<=n; p++)
      { if (prime[p])
        {  cout << p << " ";
        count++;
         }
     }
     cout<<"\nTotal prime numbers are"<<count<<"\n";
     write<<n<<"\t"<<count<<endl;
     write.close();
}
 
int main()
{
    int n;
     cout<<"\nEnter the range";
     cin>>n;
    SieveOfEratosthenes(n);







    return 0;
}
