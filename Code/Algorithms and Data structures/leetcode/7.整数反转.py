#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            is_neg = True
        y = int(str(abs(x))[::-1])

        y = y if not is_neg else -y
        
        if -2 ** 31 < y < 2 ** 31 - 1:
            return y
        return 0
# @lc code=end

