#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (40.47%)
# Likes:    687
# Dislikes: 271
# Total Accepted:    69.7K
# Total Submissions: 171.1K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 
# 
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution:
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        def util(node):
            if node is None:
                return []
            else:
                l = util(node.left)
                r = util(node.right)
                return l+r+[node.val]

        lst = Counter(util(root))
        mode = max(lst.values())
        ans = []
        for i,v in lst.items():
            if v==mode:
                ans.append(i)
        return ans

# @lc code=end

