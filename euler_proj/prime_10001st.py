#!/usr/bin/env python3

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# we have the following asymptotic bound on the nth prime pn: 
# nln(n)+n(ln(ln(n))−1)<pn<nln(n)+nln(ln(n)) for n≥6

from math import log, floor, sqrt

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

def find_nth_prime(n=10001):
    if n<=6:
        return [2,3,5,7,11,13][n-1]

    low = int(n*log(n)+n*(log(log(n))-1))+1
    cur=low
    if cur%2==0:
        cur+=1
    high = int(n*log(n)+n*log(log(n)))+1
    curIdx = None
    print("low/high bounds:{} and {}".format(low,high))
    while cur<high:
        if is_prime(cur):
            if curIdx is not None:
                curIdx+=1
                print("curIdx={}".format(curIdx))
                if curIdx==n:
                    return cur
            else:#Sieve Of Eratosthenes
                lst = list(range(3,cur,2))
                bk = 0
                for p in range(3,cur,2):
                    if lst[(p-3)//2]!=0 and is_prime(p):
                        bk+=1
                        q=p*3
                        while q<=cur:
                            lst[(q-3)//2]=0
                            q+=2*p
                if bk+2==n:
                    return cur
                else:
                    curIdx=bk+2
                    print("curIdx={}".format(curIdx))
        cur+=2


if __name__=="__main__":
    res=find_nth_prime()
    print('the 10001th prime number is {}'.format(res))