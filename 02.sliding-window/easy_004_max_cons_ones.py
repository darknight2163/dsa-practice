class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Count consecutive 1s and track the maximum streak
        max_ones = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_ones = max(max_ones, count)
            else:
                count = 0

        return max_ones