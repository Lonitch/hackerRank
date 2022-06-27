#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (63.16%)
# Likes:    461
# Dislikes: 563
# Total Accepted:    100.1K
# Total Submissions: 157.9K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# 
# Note:
# 
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if not words:
            return []
        lookup={
        'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
        'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2, 
        'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}
        ans = []
        for s in words:
            t = s.lower()
            cur = None
            i = 0
            while i < len(t):
                if cur is None:
                    cur = lookup[t[i]]
                elif cur!=lookup[t[i]]:
                    i=len(t)+10
                i+=1
            if i==len(t):
                ans.append(s)
        return ans

# @lc code=end

