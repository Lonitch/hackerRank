#!/usr/bin/env python3

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square_difference(cap=100):
    s = cap*(cap+1)//2
    res = s**2
    for p in range(1,cap+1):
        res-=p**2

    return res

if __name__=="__main__":
    num = square_difference()
    print("the difference is {}".format(num))
    