#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
# https://leetcode.com/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (52.51%)
# Likes:    635
# Dislikes: 869
# Total Accepted:    71.5K
# Total Submissions: 135.3K
# Testcase Example:  '[1,2,3,4]'
#
# You need to construct a string consists of parenthesis and integers from a
# binary tree with the preorder traversing way.
# 
# The null node needs to be represented by empty parenthesis pair "()". And you
# need to omit all the empty parenthesis pairs that don't affect the one-to-one
# mapping relationship between the string and the original binary tree.
# 
# Example 1:
# 
# Input: Binary tree: [1,2,3,4]
# ⁠      1
# ⁠    /   \
# ⁠   2     3
# ⁠  /    
# ⁠ 4     
# 
# Output: "1(2(4))(3)"
# Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to
# omit all the unnecessary empty parenthesis pairs. And it will be
# "1(2(4))(3)".
# 
# 
# 
# Example 2:
# 
# Input: Binary tree: [1,2,3,null,4]
# ⁠      1
# ⁠    /   \
# ⁠   2     3
# ⁠    \  
# ⁠     4 
# 
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we can't omit the
# first parenthesis pair to break the one-to-one mapping relationship between
# the input and the output.
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
        self.string = ""
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        def util(node):
            if node.left and node.right:
                self.string+=str(node.val)+"("
                util(node.left)
                self.string+=")("
                util(node.right)
                self.string+=")"
            elif node.left is None and node.right is None:
                self.string+=str(node.val)
            elif node.left is None:
                self.string+=str(node.val)+"()("
                util(node.right)
                self.string+=")"
            else:
                self.string+=str(node.val)+"("
                util(node.left)
                self.string+=")"
        
        util(t)
        return self.string
# @lc code=end

