class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_mapping = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_mapping:
                return [nums_mapping[diff], i]
            nums_mapping[n] = i