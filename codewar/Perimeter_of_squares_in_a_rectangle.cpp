/*
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. 
It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares ?

#Hint: See Fibonacci sequence

#Ref: http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
*/

#include <cmath>
#include <stdio.h>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>

typedef unsigned long long ull;

ull perimeter(int n)
{
    if (n==0)
    {
        return 4;
    } else if (n==1)
    {
        return 8;
    }
    
    ull first=1;
    ull second=1;
    ull curr = 0;
    ull fibsum = 2;
    for (int i = 2; i < n+1; i++)
    {
        curr = first+second;
        first = second;
        second = curr;
        fibsum+=curr;
    }

    return 4*fibsum;
}

int main()
{
    std::cout<<perimeter(8)<<std::endl;
    std::cout<<perimeter(5)<<std::endl;
    std::cout<<perimeter(2)<<std::endl;
    std::cout<<perimeter(0)<<std::endl;
    return 0;
}
