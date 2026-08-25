# Problem: Search for a target value in a sorted array and return
#          its index. Return -1 if the target does not exist.
# Approach: Use binary search by repeatedly checking the middle element.
#           If the target is smaller, search the left half; otherwise,
#           search the right half.
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        mid = (low + high) // 2

        while low <= high:
            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                high = mid - 1
                mid = (low + high) // 2

            else:
                low = mid + 1
                mid = (low + high) // 2

        return -1