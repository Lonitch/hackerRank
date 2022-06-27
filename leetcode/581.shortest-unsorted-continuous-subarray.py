#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (30.58%)
# Likes:    1985
# Dislikes: 97
# Total Accepted:    94.1K
# Total Submissions: 307.2K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        z=[x for _,x in sorted(zip(nums,range(len(nums))))]
        d = 0
        head = -1
        for i,v in enumerate(z):
            if i!=v:
                if head<0:
                    head=i
                else:
                    d=max(d,i-head+1)
        return d


# @lc code=end

