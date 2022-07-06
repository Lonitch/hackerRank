#!/usr/bin/env python3


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# According to Euclid's formula, the following equations generate triplets uniquely:
# a=k*(m^2-n^2), b=k*(2mn), c=k*(m^2+n^2)
# where k,m,and n are positive integers. Than a+b+c=k(2m^2+2mn)=1000-->km(m+n)=500
# if we let s=m+n, and we have m<s<2m(as m>n). Also, 500 must be divisible by k,m,and s.
# So we need to find all the numbers that divide 500, and from which we can find an
# appropriate combination of k,m, and s.

from math import sqrt

def find_triplet(num=1000):
    if num%2!=0:
        print('Invalid Sum, Try again!')
        return None
    kms = num//2
    cap = int(sqrt(kms))
    dvlst = []
    for p in range(2,cap+1):
        if kms%p==0:
            dvlst.append(p)
            dvlst.append(kms//p)
    dvlst = [1]+sorted(dvlst)
    prods = []
    triplet = []
    for i,m in enumerate(dvlst):
        j = i+1
        while j<len(dvlst) and dvlst[j]<2*m:
            s= dvlst[j]
            k = kms//m//s
            if k>0:
                n = s-m
                a,b,c = k*(m**2-n**2),k*(2*m*n),k*(m**2+n**2)
                if a*b*c not in prods:
                    prods.append(a*b*c)
                    triplet.append(tuple(sorted([a,b,c])))
            j+=1
    return prods, triplet

if __name__=="__main__":
    products, triplets=find_triplet()
    print("abc could be:{}".format(products))
    print("their corresponding triplets are {}".format(triplets))
        
