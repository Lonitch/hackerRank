#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (31.89%)
# Likes:    650
# Dislikes: 647
# Total Accepted:    82.5K
# Total Submissions: 257.5K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        sa = set(A)
        sb = set(B)
        if len(sa)<len(sb):
            return -1
        la = len(A)
        lb = len(B)
        if lb<=la:
            t = A*2
            if B in A:
                return 1
            elif B in t:
                return 2
            else:
                return -1
        else:
            for r in range(lb//la,lb//la+la):
                t1 = A*r
                if B in t1:
                    return r
        return -1
# @lc code=end

