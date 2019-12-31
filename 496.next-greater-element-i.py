#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (61.16%)
# Likes:    1077
# Dislikes: 1674
# Total Accepted:    122.8K
# Total Submissions: 199.4K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2. 
# 
# 
# 
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
# 
# 
# Example 1:
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
# ⁠   For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
# ⁠   For number 1 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# Example 2:
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
# ⁠   For number 2 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# 
# Note:
# 
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
# 
# 
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        i = 0
        j = nums2.index(nums1[i])
        ans = []
        while i<len(nums1):
            if nums1[i]<nums2[j]:
                ans.append(nums2[j])
                i += 1
                if i<len(nums1):
                    j = nums2.index(nums1[i])
            elif j==len(nums2)-1:
                ans.append(-1)
                i+=1
                if i<len(nums1):
                    j = nums2.index(nums1[i])
            else:
                j+=1
        return ans
# @lc code=end

