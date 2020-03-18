#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (66.35%)
# Likes:    493
# Dislikes: 433
# Total Accepted:    55.2K
# Total Submissions: 81.7K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]\r'
#
# Given a binary search tree, rearrange the tree in in-order so that the
# leftmost node in the tree is now the root of the tree, and every node has no
# left child and only 1 right child.
# 
# 
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
# ⁠      5
# ⁠     / \
# ⁠   3    6
# ⁠  / \    \
# ⁠ 2   4    8
# /        / \ 
# 1        7   9
# 
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# ⁠1
# \
# 2
# \
# 3
# \
# 4
# \
# 5
# \
# 6
# \
# 7
# \
# 8
# \
# ⁠                9  
# 
# Constraints:
# 
# 
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def util(node,lst):
            if node is not None:
                util(node.left,lst)
                lst.append(node.val)
                util(node.right,lst)

        arr = []
        util(root,arr)
        nr = TreeNode(arr[0])
        temp = nr
        for n in arr[1:]:
            temp.right=TreeNode(n)
            temp = temp.right
        return nr
# @lc code=end

