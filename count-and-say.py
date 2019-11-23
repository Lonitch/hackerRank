#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (42.23%)
# Likes:    951
# Dislikes: 7633
# Total Accepted:    331.7K
# Total Submissions: 784.8K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        first5 = ['1','11','21','1211','111221']
        if n<=5:
            return first5[n-1]
        curr = '111221'
        for i in range(5,n):
            temp=''
            count = 1
            for j in range(1,len(curr)):
                if curr[j]!=curr[j-1]:
                    temp+=str(count)+str(curr[j-1])
                    count=1
                else:
                    count+=1
            curr = temp + str(count)+str(curr[-1])
        return curr
        
# @lc code=end

