#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (31.46%)
# Likes:    619
# Dislikes: 315
# Total Accepted:    82.8K
# Total Submissions: 263.2K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# 
# 
# Note:
# 
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = 1
        if not flowerbed:
            return False
        if n==0:
            return True
        flowerbed = [0]+flowerbed+[0]
        while f<len(flowerbed)-1:
            if flowerbed[f]==0:
                if flowerbed[f-1]+flowerbed[f+1]==0:
                    n-=1
                    if n==0:
                        return True
                    flowerbed[f]=1
            f+=1
        return False

# @lc code=end

