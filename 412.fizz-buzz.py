#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (60.41%)
# Likes:    654
# Dislikes: 954
# Total Accepted:    261.4K
# Total Submissions: 431.3K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
# 
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n==0:
            return []
        ans = []
        for i in range(1,n+1):
            if i%3==i%5==0:
                ans.append('FizzBuzz')
            elif i%3==0:
                ans.append('Fizz')
            elif i%5==0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans
# @lc code=end

