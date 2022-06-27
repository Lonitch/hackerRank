#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (49.17%)
# Likes:    215
# Dislikes: 442
# Total Accepted:    48.7K
# Total Submissions: 98.7K
# Testcase Example:  '[5,4,3,2,1]'
#
# 
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
# 
# Example 1:
# 
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
# 
# 
# 
# Note:
# 
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
# 
# 
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranks = {num:r+1 for r, num in enumerate(sorted(nums, reverse=True))}
        map_rank = lambda r : ["Gold Medal", "Silver Medal", "Bronze Medal"][r-1] if r <= 3 else str(r)
        return [map_rank(ranks[num]) for num in nums]
# @lc code=end

