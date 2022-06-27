#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (46.32%)
# Likes:    480
# Dislikes: 589
# Total Accepted:    50.2K
# Total Submissions: 106.9K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        wset = set(words)
        res = ""
        for w in words:
            isIn = True
            for i in range(1, len(w)):
                if w[:i] not in wset:
                    isIn = False
                    break
            if isIn:
                if not res or len(w) > len(res):
                    res = w
                elif len(w) == len(res) and res > w:
                    res = w
        return res


# @lc code=end

