#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Easy (61.27%)
# Likes:    1426
# Dislikes: 147
# Total Accepted:    84.9K
# Total Submissions: 137.6K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# 
# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L). You might
# need to change the root of the tree, so the result should return the new root
# of the trimmed binary search tree.
# 
# 
# Example 1:
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 0   2
# 
# ⁠ L = 1
# ⁠ R = 2
# 
# Output: 
# ⁠   1
# ⁠     \
# ⁠      2
# 
# 
# 
# Example 2:
# 
# Input: 
# ⁠   3
# ⁠  / \
# ⁠ 0   4
# ⁠  \
# ⁠   2
# ⁠  /
# ⁠ 1
# 
# ⁠ L = 1
# ⁠ R = 3
# 
# Output: 
# ⁠     3
# ⁠    / 
# ⁠  2   
# ⁠ /
# ⁠1
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
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def util(node,L,R):
            if node is None:
                return None
            if L<=node.val<=R:
                node.left=util(node.left,L,R)
                node.right=util(node.right,L,R)
                return node
            elif node.val<L:
                node = util(node.right, L, R)
                return node
            elif node.val>R:
                node = util(node.left,L,R)
                return node
            
        return util(root,L,R)
                    
# @lc code=end

