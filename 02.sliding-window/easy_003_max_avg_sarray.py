from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding window: maintain the sum of each window of size k
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

s1 = Solution()
print(s1.findMaxAverage([1,12,-5,-6,50,3], 4))  # Output: 12.75
