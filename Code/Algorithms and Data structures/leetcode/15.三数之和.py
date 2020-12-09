#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1 ,0, 1, 1, 2]
        # 双指针
        nums.sort()

        len_nums = len(nums)

        if len_nums < 3:
            return []
        
        if all([i == 0 for i in nums]):
            return [[0, 0, 0]]
        
        res, k = [], 0

        # k(left p) < i(move p) < j(right p)
        for k in range(len_nums - 2):
            if nums[k] > 0:
                # 最小的都大于0, 不可能和为0了
                break
                
            if nums[k] == nums[k - 1]:
                # 避免重复
                continue
            
            i, j = k + 1, len_nums - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    # i 右移
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    # j 左移
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # i 右移
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    # j 左移
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return res
# @lc code=end

