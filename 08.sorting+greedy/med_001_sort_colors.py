# Dutch National Flag Problem --------------------
# Problem: Sort an array containing only 0s, 1s, and 2s in-place
#          without using the built-in sort function.
# Approach: Use three pointers:
#           low  -> position for 0
#           mid  -> current element being processed
#           high -> position for 2
#           0 is moved to the left, 2 to the right, and 1 stays in the middle.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        return nums