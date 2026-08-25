# Problem: Find the only number that appears once when every other
#          number appears exactly twice.
# Approach: Use XOR. XOR of a number with itself is 0, and XOR with 0
#           returns the number. Therefore, all duplicate numbers cancel
#           out and only the single number remains.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in range(1, len(nums)):
            ans = ans ^ nums[i]

        return ans