class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i  # {3:0, 2:1, 4:2}
        for i in range(len(nums)):
            rem = target - nums[i] # 3
            if rem in dic and dic[rem]!=i:
                return [i, dic[rem]]
        return []