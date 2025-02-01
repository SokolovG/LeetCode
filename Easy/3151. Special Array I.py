from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        left = 0
        right = 1

        while right < len(nums):
            if (nums[left] + nums[right] ) % 2 == 0:
                return False
            left += 1
            right += 1
        return True
