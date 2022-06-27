#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (42.86%)
# Likes:    1703
# Dislikes: 76
# Total Accepted:    161.7K
# Total Submissions: 371.8K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
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
        self.rtval=0
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        self.rtval=t.val
        def cpr(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 and n2:
                if n1.val==n2.val:
                    return (cpr(n1.left,n2.left) and cpr(n1.right,n2.right)) or cpr(n1.left,n2) or cpr(n1.right,n2)
                elif n2.val==self.rtval:
                    return cpr(n1.left,n2) or cpr(n1.right,n2)
                else:
                    return False
            else:
                return False
        return cpr(s,t)
# @lc code=end

