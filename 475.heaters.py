#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (32.46%)
# Likes:    579
# Dislikes: 634
# Total Accepted:    56.2K
# Total Submissions: 172.8K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
# 
# Note:
# 
# 
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0
        heaters.sort()
        ans = 0
        htlen = len(heaters)
        for h in houses:
            l = 0
            r = htlen
            # Find the nearest-neighbor heaters 
            # for each house
            while l<r:
                mid = l+(r-l)//2
                if heaters[mid]<h:
                    l = mid+1
                else:
                    r = mid
            # Calculate the distance between the house
            # and the heaters, use the smaller one
            if r==htlen:
                d1 = 2**31
            else:
                d1 = heaters[r]-h
            if r==0:
                d2 = 2**31
            else:
                d2 = h-heaters[r-1]
            # compare current distance with previous ones
            # use the larger one
            ans = max(ans,min(d1,d2))
        return ans
# @lc code=end

