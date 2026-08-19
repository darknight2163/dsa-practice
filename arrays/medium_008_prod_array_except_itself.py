class Solution:
    """
    For every index i:
    answer[i] = product of elements BEFORE i  
                            x 
                product of elements AFTER i
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre_arr = [1]*n
        suff_arr = [1]*n
        for i in range(1,n):
            # 1 1 2 6
            pre_arr[i]=pre_arr[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            # 24 12 4 1
            suff_arr[j]=suff_arr[j+1]*nums[j+1]
        
        for i in range(n):
            nums[i]=pre_arr[i]*suff_arr[i]
        
        return nums