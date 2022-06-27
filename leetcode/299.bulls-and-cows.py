#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Easy (40.85%)
# Likes:    455
# Dislikes: 505
# Total Accepted:    121.1K
# Total Submissions: 295.6K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# 
# Output: "1A3B"
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# 
# Output: "1A1B"
# 
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
# 
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if secret=='' or guess=='':
            return '0A0B'
        ct1 = defaultdict(list)
        ct2 = Counter(secret)
        ct3 = Counter(guess)
        ans = defaultdict(int)
        for i,s in enumerate(secret):
            ct1[s].append(i)
        for i,s in enumerate(guess):
            if i in ct1[s]:
                ct1[s].remove(i)
                ct2[s]-=1
                ct3[s]-=1
                ans['A']+=1
        for s in ct3.keys():
            ans['B']+=min(ct2[s],ct3[s])
        return str(ans['A'])+'A'+str(ans['B'])+'B'
        
# @lc code=end

