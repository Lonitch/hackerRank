#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (49.06%)
# Likes:    467
# Dislikes: 172
# Total Accepted:    74.5K
# Total Submissions: 150.5K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n' +
  '["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings. 
# 
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# 
# Example 1:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# 
# Example 2:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# 
# 
# Note:
# 
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2:
            return []
        ct = defaultdict(int)
        lids = 2**31
        ans = []
        for i,v in enumerate(list1):
            ct[v]=i+1
        for i,v in enumerate(list2):
            if ct[v]>0:
                cs = i+ct[v]-1
                if cs == lids:
                    ans.append(v)
                if cs<lids:
                    ans = [v]
                    lids = cs
        return ans
# @lc code=end

