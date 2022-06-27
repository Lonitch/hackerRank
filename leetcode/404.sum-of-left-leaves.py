#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (49.86%)
# Likes:    825
# Dislikes: 96
# Total Accepted:    148.3K
# Total Submissions: 296.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def util(node,s):
            if node.left is None and node.right is None:
                return node.val*(s==1)
            elif node.left is None:
                return util(node.right,2)
            elif node.right is None:
                return util(node.left,1)
            else:
                return util(node.left,1)+util(node.right,2)

        return util(root,0)

# @lc code=end

