#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#
# https://leetcode.com/problems/reorder-data-in-log-files/description/
#
# algorithms
# Easy (54.01%)
# Likes:    456
# Dislikes: 1420
# Total Accepted:    88.6K
# Total Submissions: 165.5K
# Testcase Example:  '["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]'
#
# You have an array of logs.  Each log is a space delimited string of words.
# 
# For each log, the first word in each log is an alphanumeric identifier.
# Then, either:
# 
# 
# Each word after the identifier will consist only of lowercase letters,
# or;
# Each word after the identifier will consist only of digits.
# 
# 
# We will call these two varieties of logs letter-logs and digit-logs.  It is
# guaranteed that each log has at least one word after its identifier.
# 
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the
# identifier used in case of ties.  The digit-logs should be put in their
# original order.
# 
# Return the final order of the logs.
# 
# 
# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit
# dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5
# 1","dig2 3 6"]
# 
# 
# Constraints:
# 
# 
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the
# identifier.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        llog = defaultdict(list)
        nlog = []
        ans = []
        for s in logs:
            cur = s.split()
            if cur[1][0] in 'abcdefghijklmnopqrstuvwxyz':
                llog[' '.join(cur[1:])].append(cur[0])
            else:
                nlog.append(s)

        lsort = list(llog.keys())
        lsort.sort()

        for c in lsort:
            temp = llog[c]
            temp.sort()
            for i in temp:
                ans.append(i+' '+c)

        return ans+nlog
# @lc code=end

