#!/usr/bin/env python3

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from math import sqrt,floor

def last_palindrom(num):
    for m in range(num-1,num//2,-1):
        if str(m)==str(m)[::-1]:
            return m

def find_palindrom(d=3):
    cap = (10**d-1)**2
    s = 10**d-1
    palin = last_palindrom(cap)
    while True:
        while palin%s!=0 and 10**(d-1)-1<s<10**d and 10**(d-1)-1<palin//s<10**d:
            s-=1
        if 10**(d-1)-1<s<10**d and 10**(d-1)-1<palin//s<10**d:
            return palin, s, palin//s
        else:
            palin = last_palindrom(palin)
            s = floor(sqrt(palin))+1
            print("cur palindrom {}".format(palin))
            
        
    


    

if __name__=="__main__":
    p, a, b = find_palindrom(5)
    print("num={},a={},b={}".format(p,a,b))