#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.99%)
# Likes:    394
# Dislikes: 147
# Total Accepted:    131.7K
# Total Submissions: 257.6K
# Testcase Example:  '"a"\n"b"'
#
# 
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return
# false. 
# 
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for s in c1.keys():
            if c1[s]>c2[s]:
                return False
        return True
# @lc code=end

