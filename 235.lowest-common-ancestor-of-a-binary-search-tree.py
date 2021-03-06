#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (46.99%)
# Likes:    1432
# Dislikes: 91
# Total Accepted:    337.3K
# Total Submissions: 714.2K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # METHOD FOR BINARY TREE
        # def util(node,n1,n2):
        #     if node is None:
        #         return None
        #     if node.val in [n1.val,n2.val]:
        #         return node
        #     else:
        #         left = util(node.left,n1,n2)
        #         right = util(node.right,n1,n2)
        #         if left is None and right is None:
        #             return None
        #         elif left is None:
        #             return right
        #         elif right is None:
        #             return left
        #         else:
        #             return node
        # return util(root,p,q)

        # METHOD USING BST PROPERTIES
        def util(node,a,b):
            if node is None:
                return None
            if node.val < min(a,b):
                return util(node.right,a,b)
            if node.val > max(a,b):
                return util(node.left, a,b)
            return node
        return util(root,p.val,q.val)
# @lc code=end

