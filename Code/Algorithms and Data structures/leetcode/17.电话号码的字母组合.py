#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        # if len(digits) == 0:
        #     return []

        # if len(digits) == 1:
        #     return list(d[digits[0]])

        # prev = self.letterCombinations(digits[:-1])
        # additional = d[digits[-1]]

        # return [s + c for s in prev for c in additional]

        # letters = ['abc', 'def', 'wxyz']

        # me
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(d[digits[0]])

        result = list(d[digits[0]])
        letters = [d[i] for i in digits][1:]
        while letters:
            additional = letters[0]
            result = [s + c for s in result for c in list(additional)]
            letters = letters[1:]

        return result
# @lc code=end

