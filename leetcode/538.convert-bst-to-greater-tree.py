#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (52.75%)
# Likes:    1583
# Dislikes: 101
# Total Accepted:    101.1K
# Total Submissions: 190.2K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
        self._sum = 0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        self.convertBST(root.right)
        self._sum += root.val
        root.val = self._sum
        self.convertBST(root.left)
        return root
    # def convertBST(self, root: TreeNode) -> TreeNode:
    #     if root is None:
    #         return root
    #     def util(node):
    #         if node is None:
    #             return []
    #         return [node.val]+util(node.left)+util(node.right)

    #     def assign(node,dic):
    #         if node is not None:
    #             node.val=dic[node.val]
    #             assign(node.left,dic)
    #             assign(node.right,dic)

    #     vals = util(root)
    #     vals = list(set(vals))
    #     vals.sort()
    #     tb = {}
    #     for i,v in enumerate(vals):
    #         if i<len(vals)-1:
    #             tb[v]=v+sum(vals[i+1:])
    #         else:
    #             tb[v]=v
    #     assign(root,tb)
    #     return root

# @lc code=end

