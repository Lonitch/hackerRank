#!/usr/bin/env python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt,ceil

def is_prime(num,f=2):
    if num <2:
        return False

    if num in [2,3] or f>sqrt(num):
        return True
    elif num%f==0:
        return False
    else:
        return is_prime(num,f+1)


def sieve(cap=2000000):
    lst = list(range(3,cap,2))
    for i in range(3,ceil(cap/3),2):
        if is_prime(i):
            p = i+2*i
            while p<cap:
                lst[(p-3)//2]=0
                p+=2*i
    return sum(lst)+2,lst
    
if __name__=="__main__":
    s,lst=sieve()
    print(lst[:100])
    print('the sum of prime numbers that < 2000000 is {}'.format(s))