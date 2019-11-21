/*
Consider a sequence u where u is defined as follows:

    The number u(0) = 1 is the first one in u.
    For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    There are no other numbers in u.

Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
Example:

dbl_linear(10) should return 22
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;

int dblLinear(int n)
{
    std::vector<long long> tlst={1,3,4,7,9,10,13,15,19,21,22};
    if (n<=10)
    {
        return tlst[n];
    }
    int x2c = 6;
    int x3c = 4;
    int curr = 11;
    while (curr<=n)
    {
        if (2*tlst[x2c]+1==tlst.back())
        {
           x2c++;
        } 
        if (3*tlst[x3c]+1==tlst.back())
        {
            x3c++;
        }
        
        if (2*tlst[x2c]+1<=3*tlst[x3c]+1)
        {
            tlst.push_back(2*tlst[x2c]+1);
            cout<<2*tlst[x2c]+1<<endl;
            x2c++;
            
        }else
        {
            tlst.push_back(3*tlst[x3c]+1);
            cout<<3*tlst[x3c]+1<<endl;
            x3c++;
        }
        
        curr++; 
    }
    
    return tlst.back();
}

int main(){
    int t = 30;
    int res = dblLinear(t);
    cout<<res<<endl;
    return 0;
}