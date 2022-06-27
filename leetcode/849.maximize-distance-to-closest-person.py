#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (41.76%)
# Likes:    626
# Dislikes: 95
# Total Accepted:    52.1K
# Total Submissions: 123.5K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# In a row of seats, 1 represents a person sitting in that seat, and 0
# represents that the seat is empty. 
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to closest person.
# 
# 
# Example 1:
# 
# 
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has
# distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# Note:
# 
# 
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        st = ''.join([str(i) for i in seats])
        sst = st.split('1')
        sst =list(filter(None,sst))
        ms = max([len(t) for t in sst])
        fs = len(sst[0])
        fs = fs*(st[:fs]==sst[0])
        ls = len(sst[-1])
        ls = ls*(st[-ls:]==sst[-1])
        if ms%2==0:
            return max([ms//2,fs,ls])
        else:
            return max([ms//2+1,fs,ls])

# @lc code=end

