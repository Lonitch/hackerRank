#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (43.07%)
# Likes:    482
# Dislikes: 719
# Total Accepted:    64K
# Total Submissions: 148.8K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property root.val =
# min(root.left.val, root.right.val) always holds.
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
# 
# 
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

class Solution:
    def __init__(self):
        self.min1 = 2**31
        self.min2 = 2**31
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def util(node):
            if node.left is not None:
                if node.val<=self.min1:
                    self.min1= node.val
                    if node.left.val != node.right.val:
                        self.min2 = min(self.min2,max(node.left.val,node.right.val))
                    util(node.left)
                    util(node.right)
                elif node.val<self.min2:
                    self.min2 = node.val
                    util(node.left)
                    util(node.right)
        util(root)
        if self.min2==2**31:
            return -1
        else:
            return self.min2
# @lc code=end

