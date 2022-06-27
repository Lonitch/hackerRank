/*

Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

Examples:

2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"

*/

#include <cmath>
#include <stdio.h>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>

std::string uint32_to_ip(uint32_t ip)
{
  int digits[32];
  int i=0;
  while (i<32)
  {
      digits[i]=ip%2;
      i++;
      ip=ip/2;
  }
  std::string ans="";
  int c=0;
  int p=0;
  for (int j = 0; j < 32; j++)
  {
      if (digits[j]==1)
      {
          c=c+(int)std::pow(2,p);
      }
      p++;
      if (j>0 && (j+1)%8==0)
      {
          ans = std::to_string(c)+"."+ans;
          c=0;
          p=0;
      }
      
  }
  ans.pop_back();
  return ans;
  
}

std::string uint32_to_ip_2(uint32_t ip)
{
  std::string result;
  result= std::to_string(ip >> 24) + '.' + std::to_string(ip >> 16 & 0xFF) + '.' +
  std::to_string(ip >> 8 & 0xFF ) + '.' + std::to_string(ip & 0xFF);
  return result;
}

int main()
{
    std::string t = uint32_to_ip(2149583361);
    std::string t2 = uint32_to_ip_2(2149583361);
    std::cout<<t<<std::endl;
    std::cout<<t2<<std::endl;
    return 0;
}