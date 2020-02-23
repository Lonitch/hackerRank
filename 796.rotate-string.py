#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.34%)
# Likes:    557
# Dislikes: 43
# Total Accepted:    56.2K
# Total Submissions: 113.5K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
# 
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
# 
# 
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
# 
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# 
# 
# Note:
# 
# 
# A and B will have length at most 100.
# 
# 
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        elif not A or not B:
            return False
        lead = B[0]
        t = []
        for i,c in enumerate(A):
            if c==lead:
                temp = A[i:]+A[:i]
                if temp==B:
                    return True
        return False
        
# @lc code=end

