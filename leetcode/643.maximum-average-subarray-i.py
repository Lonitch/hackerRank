#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (40.45%)
# Likes:    570
# Dislikes: 93
# Total Accepted:    65.5K
# Total Submissions: 160.8K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# Example 1:
# 
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k>len(nums):
            return 0
        ans = sum(nums[:k])
        cur = sum(nums[:k])
        t0 = 0
        t1 = k
        while t1<len(nums):
            cur = cur-nums[t0]+nums[t1]
            ans = max(ans,cur)
            t1+=1
            t0+=1
        return ans/k
# @lc code=end

