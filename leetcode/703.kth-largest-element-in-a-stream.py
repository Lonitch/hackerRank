#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (47.37%)
# Likes:    500
# Dislikes: 264
# Total Accepted:    58.5K
# Total Submissions: 121.6K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n' +
  '[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
# 
# Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For
# each call to the method KthLargest.add, return the element representing the
# kth largest element in the stream.
# 
# Example:
# 
# 
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 
# 
# Note: 
# You may assume that nums' length ≥ k-1 and k ≥ 1.
# 
#

# @lc code=start
import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.lst = nums[-k:]

    def add(self, val: int) -> int:
        if len(self.lst)<self.k:
            bisect.insort(self.lst, val)
            return self.lst[0]

        if val>self.lst[0]:
            self.lst.pop(0)
            bisect.insort(self.lst, val)
            return self.lst[0]
        else:
            return self.lst[0]  


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

