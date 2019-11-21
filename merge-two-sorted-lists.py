#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (49.92%)
# Likes:    2925
# Dislikes: 423
# Total Accepted:    751.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val<l2.val:
            head = ListNode(l1.val)
            c1 = l1.next
            c2 = l2
        else:
            head = ListNode(l2.val)
            c2 = l2.next
            c1 = l1
        temp = head
        while c1 is not None or c2 is not None:
            if c1 is not None and c2 is not None:
                if c1.val<c2.val:
                    temp.next = ListNode(c1.val)
                    c1 = c1.next
                    temp = temp.next
                else:
                    temp.next = ListNode(c2.val)
                    c2 = c2.next
                    temp = temp.next
            elif c1 is None:
                temp.next = ListNode(c2.val)
                c2 = c2.next
                temp = temp.next
            else:
                temp.next = ListNode(c1.val)
                c1 = c1.next
                temp = temp.next
        return head
# @lc code=end

