#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (51.78%)
# Likes:    662
# Dislikes: 52
# Total Accepted:    73.9K
# Total Submissions: 141.9K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note: There are at least two nodes in this BST.
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def util(node):
            if node is None:
                return []
            else:
                return [node.val]+util(node.left)+util(node.right)
        lst = util(root)
        lst.sort()
        ans = 2**31
        for i in range(1,len(lst)):
            if lst[i]-lst[i-1]<ans:
                ans = lst[i]-lst[i-1]
        return ans
# @lc code=end

