#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (46.74%)
# Likes:    867
# Dislikes: 311
# Total Accepted:    93.4K
# Total Submissions: 199.7K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array, find three numbers whose product is maximum and
# output the maximum product.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: 6
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: 24
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given array will be in range [3,10^4] and all elements are
# in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of
# 32-bit signed integer.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        return max(nums[0]*nums[1]*nums[2],nums[0]*nums[-1]*nums[-2])

        
# @lc code=end

