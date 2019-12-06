#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (36.68%)
# Likes:    1067
# Dislikes: 60
# Total Accepted:    266.1K
# Total Submissions: 724.2K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val==val:
            head = head.next
        temp = head
        while temp is not None:
            if temp.next is not None and temp.next.val==val:
                temp.next = temp.next.next
            else:
                temp=temp.next
        return head
# @lc code=end

