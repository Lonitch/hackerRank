#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (39.14%)
# Likes:    1253
# Dislikes: 394
# Total Accepted:    377.4K
# Total Submissions: 961.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def depSum(node,val,target):
            if node is None:
                return val==target
            elif node.left is None and node.right is None:
                return (val+node.val)==target
            elif node.left is None:
                return depSum(node.right,val+node.val, target)
            elif node.right is None:
                return depSum(node.left,val+node.val, target)
            else: 
                return depSum(node.left,val+node.val, target) or depSum(node.right,val+node.val, target)
        return depSum(root,0,sum)
# @lc code=end

