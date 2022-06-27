#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (54.53%)
# Likes:    2091
# Dislikes: 192
# Total Accepted:    196.4K
# Total Submissions: 358.8K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Method 1: Use set object
        # ans = set(range(1, len(nums)+1))
        # return list(ans.difference(set(nums)))

        # Method 2: Move numbers to their correct locations
        for v in nums:
            i = abs(v)-1
            if nums[i]>0:
                nums[i]=-nums[i]
        ans = []
        for i,v in enumerate(nums):
            if v>0:
                ans.append(i+1)
        return ans

# @lc code=end

