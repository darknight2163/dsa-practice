class Solution:
    """
    KADANE'S ALGORITHM:
    At each index, decide whether to extend the previous subarray
    or start a new subarray from the current element.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        last_best = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            choice1 = nums[i] + last_best
            choice2 = nums[i]
            last_best = max(choice1, choice2)
            ans = max(ans, last_best)
        
        return ans