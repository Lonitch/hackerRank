#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.75%)
# Likes:    1077
# Dislikes: 1856
# Total Accepted:    473.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = (digits[-1]+1)//10
        if carry==0:
            digits[-1]+=1
            return digits
        else:
            for i in range(n-1,-1,-1):
                curr = digits[i]+carry
                carry = curr//10
                if carry==0:
                    digits[i]=curr
                    return digits
                else:
                    digits[i]=curr%10
                    if i==0:
                        return [carry]+digits

            
# @lc code=end

