#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (45.01%)
# Likes:    577
# Dislikes: 105
# Total Accepted:    88.3K
# Total Submissions: 195.3K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its
# length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4. 
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length
# is 1. 
# 
# 
# 
# Note:
# Length of the array will not exceed 10,000.
# 
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        cur = 1
        if not nums:
            return ans
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                ans = max(ans,cur)
                cur=1
            else:
                cur+=1
        return max(cur,ans)
# @lc code=end

