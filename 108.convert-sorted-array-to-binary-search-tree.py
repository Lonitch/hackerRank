#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (53.58%)
# Likes:    1582
# Dislikes: 161
# Total Accepted:    319.1K
# Total Submissions: 593.8K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = 0
        r = len(nums)-1
        if r==l:
            return TreeNode(nums[0])
        def util(lst,left,right):
            if left<right:
                mid = left+(right-left)//2
                if left==mid:
                    curr = TreeNode(lst[right])
                    curr.left = TreeNode(lst[left])
                    return curr
                else:
                    curr = TreeNode(lst[mid])
                    curr.left = util(lst,left,mid-1)
                    curr.right = util(lst,mid+1,right)
                    return curr
            elif left==right:
                return TreeNode(lst[left])
        return util(nums,l, r)

# @lc code=end

