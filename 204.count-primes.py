#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.14%)
# Likes:    1412
# Dislikes: 476
# Total Accepted:    287.8K
# Total Submissions: 952.7K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        elif n<=7:
            t = [2,3,5]
            ans=0
            for i in t:
                ans+=(i<n)
            return ans

        def isPrime(m):
            j=1
            if m%6 not in [5,1]:
                return 0
            else:
                for j in range(2,int(m**0.5)+1):
                    if m%j==0:
                        return 0
                return 1
        ans=0
        notprime = [0]*n
        
        for i in range(2, n):
            if not notprime[i] and isPrime(i):
                ans+=1

        return ans
# @lc code=end

