#!/usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

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
    

def max_prime(num=600851475143): #Sieve Of Eratosthenes
    if num==2 or num==4:
        return 2
    cap = floor(sqrt(num))
    lst = []
    lst2 = [x for x in range(3,cap+1,2)] # 2 is the only even prime
    for n in range(3,cap+1,2):
        if lst2[(n-3)//2]!=0 and is_prime(n):
            lst2[(n-3)//2]=0
            p=3*n
            while p<cap+1:
                lst2[(p-3)//2]=0
                p+=2*n
            if num%n==0:
                lst.append(n)
                print("cur max {}".format(max(lst)))
    return max(lst)


if __name__=="__main__":
    print('Largest prime factor is: {}'.format(max_prime()))