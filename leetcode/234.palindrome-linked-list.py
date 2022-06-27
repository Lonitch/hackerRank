#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (37.36%)
# Likes:    2156
# Dislikes: 300
# Total Accepted:    325.2K
# Total Submissions: 868.1K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
        n = len(vals)
        for i in range(n//2):
            if vals[i]!=vals[n-1-i]:
                return False
        return True
# @lc code=end

