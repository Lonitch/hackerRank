#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (34.69%)
# Likes:    1312
# Dislikes: 351
# Total Accepted:    76.5K
# Total Submissions: 218.3K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
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
        self.ans = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def util(node,cur,l):
            if node is None:
                return l
            else:
                if node.val==cur:
                    left=util(node.left,cur,l+1)
                    right=util(node.right,cur,l+1)
                    self.ans = max(self.ans,left+right-2*l-2)
                    return max(left,right)
                else:
                    left=util(node.left,node.val,0)
                    right=util(node.right,node.val,0)
                    self.ans = max(self.ans,left+right)
                    return l
        util(root,2**31,0)
        return self.ans
# @lc code=end

