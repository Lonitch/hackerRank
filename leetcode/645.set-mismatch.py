#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (41.23%)
# Likes:    519
# Dislikes: 269
# Total Accepted:    61.1K
# Total Submissions: 147.5K
# Testcase Example:  '[1,2,2,4]'
#
# 
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number. 
# 
# 
# 
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# 
# 
# Note:
# 
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        setsum = sum(set(nums))
        lstsum = sum(nums)
        n = len(nums)
        tot=n*(n+1)//2
        ans = [lstsum-setsum,tot-setsum]
        return ans
        
# @lc code=end

