#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.96%)
# Likes:    1321
# Dislikes: 92
# Total Accepted:    357.6K
# Total Submissions: 699.7K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        for c in ct.keys():
            if ct[c]==1:
                return s.index(c)
        return -1
# @lc code=end

