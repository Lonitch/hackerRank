#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (37.37%)
# Likes:    1447
# Dislikes: 3271
# Total Accepted:    450.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n!=0:    
            i=m-1
            j=n-1
            while j>=0 and i>=0:
                if nums2[j]>=nums1[i]:
                    nums1[i+j+1]=nums2[j]
                    j-=1
                else:
                    nums1[i+j+1]=nums1[i]
                    i-=1
            while j>=0:
                nums1[j]=nums2[j]
                j-=1

        
# @lc code=end

