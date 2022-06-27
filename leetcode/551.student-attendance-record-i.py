#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (46.09%)
# Likes:    195
# Dislikes: 712
# Total Accepted:    67.1K
# Total Submissions: 145K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        ct =Counter(s)
        if ct['A']<=1 and 'LLL' not in s:
            return True
        else:
            return False
# @lc code=end

