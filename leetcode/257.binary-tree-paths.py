#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (47.96%)
# Likes:    1159
# Dislikes: 82
# Total Accepted:    263.7K
# Total Submissions: 547.3K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        def util(node,cur):
            if node is None:
                return [cur]
            else:
                if cur=='':
                    cur = cur+str(node.val)
                else:
                    cur=cur+'->'+str(node.val)
                if node.left is None:
                    return util(node.right,cur)
                elif node.right is None:
                    return util(node.left,cur)
                else:
                    return util(node.left,cur)+util(node.right,cur)

        ans=util(root,'')

        return ans

# @lc code=end

