#!/usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import floor, sqrt

def is_prime(n,i=2):
    cap = floor(sqrt(n))
    if n==2 or n==3:
        return True
    elif n<=1:
        return False
    elif i> cap:
        return True
    else:
        if n%i==0:
            return False
        else:
            return is_prime(n,i+1)

def update_dict(cap=20):
    res = {}
    # find all the prime numbers less than cap
    for k in range(cap):
        if is_prime(k):
            res[k]=[]
    key = list(res.keys())

    for p in range(cap,1,-1):
        for k in key:
            c = 0
            while p%(k**(c+1))==0:
                c+=1
            res[k].append(c)

    return res


if __name__=="__main__":
    dic = update_dict()
    print(dic)
    num = 1
    for k,v in dic.items():
        num*=k**max(v)
    print("Smallest multiple is {}".format(num))
