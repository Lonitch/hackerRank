#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i]+=1
        for k,v in count.items():
            if v==1:
                return k
                
# Your runtime beats 83.39 % of python3 submissions
# Your memory usage beats 13.12 % of python3 submissions (15.2 MB)
# @lc code=end

