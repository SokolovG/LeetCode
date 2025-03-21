class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i in range(len(nums)):
            new_num = target - nums[i]
            if new_num in nums_dict:
                return [nums_dict[new_num], i]
            nums_dict[nums[i]] = i

s = Solution()