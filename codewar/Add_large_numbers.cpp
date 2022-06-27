/*
Write a function that returns the sum of two numbers. The input numbers are strings and the function must return a string.

    The input numbers are big.
    The input is a string of only digits
    The numbers are positives

*/
#include <cmath>
#include <stdio.h>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;


std::string add(std::string a, std::string b) {
    if (a.empty()) return b;
    else if (b.empty()) return a;
    
    string ans="";
    // Remove leading zeros
    a.erase(0, min(a.find_first_not_of('0'), a.size()-1));
    b.erase(0, min(b.find_first_not_of('0'), b.size()-1));

    int forward=0;
    int curr;
    int a_,b_;
    while (a.length()>0 || b.length()>0)
    {
        if (a.length()>0)
        {
            a_ = a.back()-'0';
            a.pop_back();
        }else
        {
            a_=0;
        }
        
        if (b.length()>0)
        {
            b_ = b.back()-'0';
            b.pop_back();
        } else
        {
            b_=0;
        }

        curr = (a_+b_+forward)%10;
        forward = (a_+b_+forward)/10;
        ans = to_string(curr)+ans;
        //cout<<a_<<','<<b_<<','<<curr<<','<<forward<<endl;
        
    }
    if (forward!=0) return to_string(forward)+ans;
    
    return ans;
}

int main ()
{
string n1 = "34567896";
string n2 = "267984623";
string z = add (n1,n2);
cout << "The result is " << z<<endl;
n1 = "020";
n2 = "05";
z = add (n1,n2);
cout << "The result is " << z<<endl;
return 0;
}