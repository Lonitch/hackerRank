#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (55.77%)
# Likes:    464
# Dislikes: 342
# Total Accepted:    164K
# Total Submissions: 293.3K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums or max(nums)==0:
            return 0
        ans,cur=1,1
        i = nums.index(1)+1
        while i<len(nums):
            if nums[i]!=1:
                ans = max(ans,cur)
                cur = 0
            else:
                cur+=1
            i+=1
        return max(ans,cur)
# @lc code=end

