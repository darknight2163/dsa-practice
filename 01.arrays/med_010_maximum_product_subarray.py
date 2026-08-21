class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Keep min and max products ending at each index because
        a negative number can turn min into max and max into min.
        """
        min_last_best = nums[0]
        max_last_best = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            choice_1 = nums[i]
            choice_2 = nums[i] * min_last_best
            choice_3 = nums[i] * max_last_best

            min_last_best = min(choice_1, choice_2, choice_3)
            max_last_best = max(choice_1, choice_2, choice_3)
            ans = max(ans, max_last_best)

        return ans