#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
# https://leetcode.com/problems/binary-watch/description/
#
# algorithms
# Easy (45.95%)
# Likes:    447
# Dislikes: 771
# Total Accepted:    72.8K
# Total Submissions: 157.9K
# Testcase Example:  '0'
#
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the
# right.
# 
# For example, the above binary watch reads "3:25".
# 
# Given a non-negative integer n which represents the number of LEDs that are
# currently on, return all possible times the watch could represent.
# 
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04",
# "0:08", "0:16", "0:32"]
# 
# 
# Note:
# 
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid,
# it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for
# example "10:2" is not valid, it should be "10:02".
# 
# 
#

# @lc code=start
from itertools import combinations
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hrlst = [1,2,4,8]
        minlst = [1,2,4,8,16,32]
        ans = []
        for h in range(min(5,num+1)):
            if h==0:
                hr=['0']
            else:
                hr=list(combinations(hrlst,h))
                hr = [str(sum(a)) for a in hr if sum(a)<12]
            m = num-h
            mins = list(combinations(minlst,m))
            mins = [str(sum(a)) for a in mins if sum(a)<60]
            minl = [len(a) for a in mins]
            ans +=[a+':'+'0'*(2-c)+b for a in hr for b,c in zip(mins,minl)]
        return ans
            
# @lc code=end

