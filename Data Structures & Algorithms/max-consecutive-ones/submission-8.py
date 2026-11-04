class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0

        for num in nums:
            if num != 1:
                counter = 0
            else:
                counter += 1
                max_counter = max(max_counter, counter)
        return max_counter
