class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set: track seen values for constant-time duplicate lookup
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False