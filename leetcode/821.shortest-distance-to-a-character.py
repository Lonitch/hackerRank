#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
# https://leetcode.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (64.71%)
# Likes:    844
# Dislikes: 69
# Total Accepted:    54.4K
# Total Submissions: 83K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.
# 
# Example 1:
# 
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 
# 
# Note:
# 
# 
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# 
# 
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        target = []
        n = len(S)
        ans = []
        for i,c in enumerate(S):
            if C==c:
                target.append(i)
        for i in range(n):
            ans.append(min([abs(i-a) for a in target]))
        return ans
# @lc code=end

