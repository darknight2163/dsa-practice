class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_num = nums[0] 
        count = 0  
        for n in nums:
            if n == curr_num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    curr_num = n
                    count = 1
                    
        return curr_num

            
            