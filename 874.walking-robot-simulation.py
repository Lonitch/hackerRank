#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#
# https://leetcode.com/problems/walking-robot-simulation/description/
#
# algorithms
# Easy (33.40%)
# Likes:    121
# Dislikes: 644
# Total Accepted:    15.3K
# Total Submissions: 44.8K
# Testcase Example:  '[4,-1,3]\n[]'
#
# A robot on an infinite grid starts at point (0, 0) and faces north.  The
# robot can receive one of three possible types of commands:
# 
# 
# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# 
# 
# Some of the grid squares are obstacles. 
# 
# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
# 
# If the robot would try to move onto them, the robot stays on the previous
# grid square instead (but still continues following the rest of the route.)
# 
# Return the square of the maximum Euclidean distance that the robot will be
# from the origin.
# 
# 
# 
# Example 1:
# 
# 
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
# 
# 
# 
# Example 2:
# 
# 
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to
# (1, 8)
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# The answer is guaranteed to be less than 2 ^ 31.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curx,cury = 0,0
        obx=defaultdict(list)
        oby=defaultdict(list)
        ans = 0
        for o in obstacles:
            obx[o[0]].append(o[1])
            oby[o[1]].append(o[0])
        mv = [0,1]
        for c in commands:
            if c==-2:
                mv[0],mv[1]=-mv[1],mv[0]
            elif c==-1:
                mv[0],mv[1]=mv[1],-mv[0]
            else:
                if mv[0]==0:
                    if obx[curx]:
                        i = 1
                        while i<=c: 
                            if cury+mv[1] in obx[curx]:
                                i=c+1
                            else:
                                cury+=mv[1]
                                i+=1
                    else:
                        cury+=c*mv[1]
                else:
                    if oby[cury]:
                        i=1
                        while i <= c: 
                            if curx+mv[0] in oby[cury]:
                                i=c+1
                            else:
                                curx+=mv[0]
                                i+=1
                    else:
                        curx+=c*mv[0]
            ans = max(ans,curx**2+cury**2)
        return ans
# @lc code=end

