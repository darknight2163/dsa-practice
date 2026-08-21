class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap + bucket sort: group numbers by frequency and pick the top k
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(nums), 0, -1):
            result.extend(buckets[count])

            if len(result) >= k:
                return result[:k]

        return result