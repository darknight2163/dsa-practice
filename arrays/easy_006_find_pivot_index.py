class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = total-nums[0]
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left = left + nums[i-1]
            right = total - left - nums[i]
            if left == right:
                return i
        return -1
        