#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
# https://leetcode.com/problems/most-common-word/description/
#
# algorithms
# Easy (43.11%)
# Likes:    490
# Dislikes: 1243
# Total Accepted:    115.9K
# Total Submissions: 265.1K
# Testcase Example:  '"Bob hit a ball, the hit BALL flew far after it was hit."\n["hit"]'
#
# Given a paragraph and a list of banned words, return the most frequent word
# that is not in the list of banned words.  It is guaranteed there is at least
# one word that isn't banned, and that the answer is unique.
# 
# Words in the list of banned words are given in lowercase, and free of
# punctuation.  Words in the paragraph are not case sensitive.  The answer is
# in lowercase.
# 
# 
# 
# Example:
# 
# 
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent
# non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is
# banned.
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= paragraph.length <= 1000.
# 0 <= banned.length <= 100.
# 1 <= banned[i].length <= 10.
# The answer is unique, and written in lowercase (even if its occurrences in
# paragraph may have uppercase symbols, and even if it is a proper noun.)
# paragraph only consists of letters, spaces, or the punctuation symbols
# !?',;.
# There are no hyphens or hyphenated words.
# Words only consist of letters, never apostrophes or other punctuation
# symbols.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        t=paragraph.replace(',',' ')
        t=t.replace('!',' ')
        t=t.replace('?',' ')
        t=t.replace("'",' ')
        t=t.replace(";",' ')
        t=t.replace(".",' ')
        t= t.lower()
        t= t.split(' ')
        t = list(filter(None,t))
        ct = Counter(t)
        num = 0
        ans = ''
        for w in ct.keys():
            if w not in banned and ct[w]>num:
                ans = w
                num = ct[w]
        return ans
# @lc code=end

