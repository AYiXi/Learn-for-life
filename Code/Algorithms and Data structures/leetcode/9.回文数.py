#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return x > -1 and str(x)[::-1] == str(x)

        # 不用字符串
        if x < 0:
            return False

        temp = x
        reverse = 0

        while(temp != 0):
            reverse = reverse * 10 + temp % 10
            temp = temp // 10

        return reverse == x
# @lc code=end
