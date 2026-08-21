class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Fixed-size sliding window: count windows whose average meets the threshold
        target = threshold * k
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= target:
            count += 1

        for right in range(k, len(arr)):
            window_sum += arr[right] - arr[right - k]

            if window_sum >= target:
                count += 1

        return count