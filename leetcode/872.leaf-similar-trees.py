#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (64.22%)
# Likes:    576
# Dislikes: 28
# Total Accepted:    71.4K
# Total Submissions: 110.2K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
  '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree.  From left to right order, the
# values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
# 
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
# 
# 
# 
# Note:
# 
# 
# Both of the given trees will have between 1 and 100 nodes.
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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def util(node,lst):
            if node.left is None and node.right is None:
                lst.append(node.val)
            else:
                if node.left is not None:
                    util(node.left,lst)
                if node.right is not None:
                    util(node.right,lst)
        nl1 = []
        nl2 = []
        util(root1,nl1)
        util(root2,nl2)
        for a,b in zip(nl1,nl2):
            if a!=b:
                return False
        return True

# @lc code=end

