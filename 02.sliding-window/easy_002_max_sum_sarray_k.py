class Solution:
    def maxSubarraySum(self, arr, k):
        # Sliding window: keep the sum of the current window of size k
        summ = 0
        
        l = len(arr)
        
        for i in range(k):
            summ += arr[i]
        max_sum = summ
        
        if l == k:
            return summ
        
        j = k
        while j<l:
            summ = summ - arr[j-k] + arr[j]
            max_sum = max(max_sum, summ)
            j+=1
        
        return max_sum
            
            
            

            
        