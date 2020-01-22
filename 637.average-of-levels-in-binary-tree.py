#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (60.26%)
# Likes:    983
# Dislikes: 140
# Total Accepted:    101.4K
# Total Submissions: 166.6K
# Testcase Example:  '[3,9,20,15,7]'
#
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.
# 
# Example 1:
# 
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
# 
# 
# 
# Note:
# 
# The range of node's value is in the range of 32-bit signed integer.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def __init__(self):
        self.ct = defaultdict(int)
        self.sum = defaultdict(int)
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        def util(node, level):
            if node:
                self.ct[level]+=1
                self.sum[level]+=node.val
                util(node.left,level+1)
                util(node.right,level+1)

        ans = []
        util(root,0)
        for i in range(max(self.ct.keys())+1):
            ans.append(self.sum[i]/self.ct[i])
        return ans
# @lc code=end

