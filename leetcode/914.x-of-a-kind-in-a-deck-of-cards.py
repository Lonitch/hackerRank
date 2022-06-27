#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (33.92%)
# Likes:    378
# Dislikes: 93
# Total Accepted:    31.3K
# Total Submissions: 92K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# In a deck of cards, each card has an integer written on it.
# 
# Return true if and only if you can choose X >= 2 such that it is possible to
# split the entire deck into 1 or more groups of cards, where:
# 
# 
# Each group has exactly X cards.
# All the cards in each group have the same integer.
# 
# 
# 
# Example 1:
# 
# 
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# 
# 
# Example 2:
# 
# 
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false´
# Explanation: No possible partition.
# 
# 
# Example 3:
# 
# 
# Input: deck = [1]
# Output: false
# Explanation: No possible partition.
# 
# 
# Example 4:
# 
# 
# Input: deck = [1,1]
# Output: true
# Explanation: Possible partition [1,1].
# 
# 
# Example 5:
# 
# 
# Input: deck = [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= deck.length <= 10^4
# 0 <= deck[i] < 10^4
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        ct = list(Counter(deck).values())
        uniq = list(set(ct))
        if 1 in uniq:
            return False
        elif len(uniq)==1:
            return True
        else:
            cur = min(ct)
            tb = [2, 3, 5, 7, 11, 
            13, 17, 19, 23, 29, 
            31, 37, 41, 43, 47, 
            53, 59, 61, 67, 71, 
            73, 79, 83, 89, 97]
            for t in tb:
                if cur%t==0:
                    i=0
                    while i<len(uniq):
                        if uniq[i]%t:
                            i = len(uniq)+1
                        else:
                            i+=1
                    if i==len(uniq):
                        return True
            return False

# @lc code=end

