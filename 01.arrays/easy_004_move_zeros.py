class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums)
        i=0
        while i<j:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                j-=1
            else:
                i+=1
        return nums