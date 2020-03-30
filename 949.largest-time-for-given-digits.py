#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (34.58%)
# Likes:    147
# Dislikes: 309
# Total Accepted:    14.6K
# Total Submissions: 40.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
# 
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
# 
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4]
# Output: "23:41"
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,5,5,5]
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if min(A)>2:
            return ""
        if max(A)==0:
            return "00:00"
        A.sort()
        A0 = A.copy()
        ans = ""
        ct = Counter(A)
        if 2 in A and (set([0,1,3]).intersection(A) or ct[2]>1):
            ans+=str(2)
            A.pop(A.index(2))
            t,t2 = -1,-1
            for d in A:
                if 0<=d<4:
                    t = max(d,t)
            ans+=str(t)+":"
            A.pop(A.index(t))
            for d in A:
                if 0<=d<6:
                    t2 = max(d,t2)
            if t2==-1:
                ans=""
            else:
                ans+=str(t2)
                A.pop(A.index(t2))
                ans+=str(A[0])
        A = A0.copy()
        if 1 in A and ans=="":
            ans+=str(1)
            A.pop(A.index(1))
            t = -1
            for d in A[:-1]:
                if 0<=d<6:
                    t = max(d,t)
            if t==-1 and A[-1]>=6:
                ans=""
            elif t==-1:
                ans+=str(max(A[:-1]))+":"+str(A[-1])
                A=A[:-1]
                A.pop(A.index(max(A)))
                ans+=str(A[0])
            else:
                ans+=str(A[-1])+":"+str(t)
                A = A[:-1]
                A.pop(A.index(t))
                ans+=str(A[0])
        A = A0.copy()
        if 0 in A and ans=="":
            ans+=str(0)
            A.pop(A.index(0))
            t = -1
            for d in A[:-1]:
                if 0<=d<6:
                    t = max(d,t)
            if t==-1 and A[-1]>=6:
                ans=""
            elif t==-1:
                ans+=str(max(A[:-1]))+":"+str(A[-1])
                A=A[:-1]
                A.pop(A.index(max(A)))
                ans+=str(A[0])
            else:
                ans+=str(A[-1])+":"+str(t)
                A = A[:-1]
                A.pop(A.index(t))
                ans+=str(A[0])
        return ans
# @lc code=end

