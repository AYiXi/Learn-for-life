#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join([i for i in s if i.isalnum()]).lower()
        return s2 == s2[::-1]
# @lc code=end

