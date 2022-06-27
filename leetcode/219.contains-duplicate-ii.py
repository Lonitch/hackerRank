#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (36.29%)
# Likes:    624
# Dislikes: 775
# Total Accepted:    229K
# Total Submissions: 629.4K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k<=0:
            return False
        ct = defaultdict(list)
        for i,n in enumerate(nums):
            if ct[n]:
                for m in ct[n]:
                    if i-m<=k:
                        return True
            ct[n].append(i)

        return False
# @lc code=end

