#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (38.70%)
# Likes:    1983
# Dislikes: 286
# Total Accepted:    495.1K
# Total Submissions: 1.3M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
# 
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# 
# 
# 
# 
# Follow up:
# 
# Can you solve it using O(1) (i.e. constant) memory?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head
        while slow is not None and fast is not None:
            if fast is not None and fast.next is not None:
                fast = fast.next.next

            if slow is not None:
                slow = slow.next

            if fast is not None and fast.next is not None and slow is not None:
                if fast.val==slow.val:
                    return True
        return False
# @lc code=end

