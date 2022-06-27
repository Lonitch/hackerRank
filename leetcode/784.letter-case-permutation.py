#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (60.11%)
# Likes:    931
# Dislikes: 95
# Total Accepted:    71.9K
# Total Submissions: 116.8K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        for i,c in enumerate(S):
            if c in 'abcdefghijklmnopqrstuvwxyz':
                cc = c.upper()
                temp = []
                for a in ans:
                    temp.append(a[:i]+cc+a[i+1:])
                ans.append(S[:i]+cc+S[i+1:])
                ans+=temp
            elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                cc = c.lower()
                temp=[]
                for a in ans:
                    temp.append(a[:i]+cc+a[i+1:])
                ans.append(S[:i]+cc+S[i+1:])
                ans+=temp

        return [S]+ans
# @lc code=end

