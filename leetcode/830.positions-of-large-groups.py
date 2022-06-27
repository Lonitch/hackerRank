#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#
# https://leetcode.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (48.35%)
# Likes:    280
# Dislikes: 76
# Total Accepted:    36.8K
# Total Submissions: 75.4K
# Testcase Example:  '"abbxxxxzzy"'
#
# In a string S of lowercase letters, these letters form consecutive groups of
# the same character.
# 
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z" and "yy".
# 
# Call a group large if it has 3 or more characters.  We would like the
# starting and ending positions of every large group.
# 
# The final answer should be in lexicographic order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending
# positions 6.
# 
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# 
# 
# Example 3:
# 
# 
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# 
# 
# 
# Note:  1 <= S.length <= 1000
# 
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        if len(S)<3:
            return ans
        i=0
        while i <len(S):
            j=3
            while S[i:i+j]==S[i]*j:
                j+=1
            if j>3:
                ans.append([i,i+j-2])
                i+=j-1
            else:
                i+=1
        return ans

# @lc code=end

