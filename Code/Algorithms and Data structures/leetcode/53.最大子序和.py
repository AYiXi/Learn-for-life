#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp_sum = 0
        for num in nums:
            temp_sum += num
            
            if temp_sum > max_sum:
                max_sum = temp_sum

            if temp_sum < 0:
                temp_sum = 0

        return max_sum
# @lc code=end

