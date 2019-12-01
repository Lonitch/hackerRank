#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.16%)
# Likes:    917
# Dislikes: 523
# Total Accepted:    344K
# Total Submissions: 950.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dep(node, d):
            if node.left is None and node.right is None:
                return d
            elif node.left is None:
                return dep(node.right,d+1)
            elif node.right is None:
                return dep(node.left,d+1)
            else:
                ldep = dep(node.left,d+1)
                rdep = dep(node.right,d+1)
                return min(ldep,rdep)
        return dep(root,1)
# @lc code=end

