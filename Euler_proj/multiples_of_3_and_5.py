#!/usr/bin/env python3

# Problem statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from pprint import pp

def fSum(f,cap=1000):
    n = int(cap/f)
    if n*f==cap:
        n-=1
    return n*(n+1)//2*f

if __name__=="__main__":
    lst = []
    d1 = 1
    while d1*3<1000 or d1*5<1000:
        if d1*3 not in lst and d1*3<1000:
            lst.append(d1*3)
        if d1*5 not in lst and d1*5<1000:
            lst.append(d1*5)
        d1+=1
    print("Number of multiples is {}".format(len(lst)))
    print("Sum of multiples is {}".format(fSum(3)+fSum(5)-fSum(15)))