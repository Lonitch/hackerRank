#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (35.03%)
# Likes:    199
# Dislikes: 531
# Total Accepted:    52.1K
# Total Submissions: 148K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=5:
            return False
        t = int(num**0.5)
        ans = 1
        for i in range(2,t+1):
            if num%i==0:
                ans+=i
                ans+=num//i
        return ans==num
# @lc code=end

