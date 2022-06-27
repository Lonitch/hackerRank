#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (57.93%)
# Likes:    3150
# Dislikes: 75
# Total Accepted:    756.5K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        temp = head
        vals = []
        while temp is not None:
            vals.append(temp.val)
            temp =temp.next
        vals = vals[::-1]
        new = ListNode(vals[0])
        temp = new
        for i in range(1,len(vals)):
            temp.next = ListNode(vals[i])
            temp = temp.next
        return new
# @lc code=end

