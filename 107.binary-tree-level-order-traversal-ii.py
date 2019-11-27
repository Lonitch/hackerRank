#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (48.90%)
# Likes:    911
# Dislikes: 171
# Total Accepted:    261.6K
# Total Submissions: 533.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
from collections import defaultdict
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def dfs(node,valst,d):
            if node is not None:
                valst[d].append(node.val)
                dfs(node.left,valst,d+1)
                dfs(node.right,valst,d+1)
        lst = defaultdict(list)
        dfs(root,lst,0)
        ans = []
        i=0
        while lst[i]:
            ans.append(lst[i])
            i+=1
        return ans[::-1]

# @lc code=end

