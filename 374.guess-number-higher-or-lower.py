#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (40.73%)
# Likes:    295
# Dislikes: 1414
# Total Accepted:    126.8K
# Total Submissions: 309.9K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example :
# 
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# 
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l<r:
            mid = (l+r)//2
            temp = guess(mid)
            if temp>0:
                l = mid+1
            elif temp==0:
                return mid
            else:
                r = mid-1
        return l
# @lc code=end

