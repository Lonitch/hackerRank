#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (52.03%)
# Likes:    697
# Dislikes: 635
# Total Accepted:    69.6K
# Total Submissions: 132.1K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
# 
# Example 1:
# 
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,2,3,1,4,2]
# Output: 6
# 
# 
# 
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
# 
#

# @lc code=start
from collections import Counter,defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ct = Counter(nums)
        deg = max(ct.values())
        elem = []
        ftid = defaultdict(list)

        for a,b in zip(ct.keys(),ct.values()):
            if b==deg:
                elem.append(a)

        for i,v in enumerate(nums):
            if v in elem:
                ftid[v].append(i)

        return min([x[-1]-x[0]+1 for x in ftid.values()])

# @lc code=end

