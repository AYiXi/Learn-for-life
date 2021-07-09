#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[n - 1]
# @lc code=end

