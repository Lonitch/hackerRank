#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (37.33%)
# Likes:    168
# Dislikes: 638
# Total Accepted:    65.7K
# Total Submissions: 175.6K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
# 
# Please note that the string does not contain any non-printable characters.
# 
# Example:
# 
# Input: "Hello, my name is John"
# Output: 5
# 
# 
#

# @lc code=start
import re
class Solution:
    def countSegments(self, s: str) -> int:
        if s=='':
            return 0
        
        return sum([1 for c in re.split(' ',s) if c!=''])
# @lc code=end

