class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        n = len(s)
        left = 0
        max_len = 0

        for i in range(n):
            if s[i] in indexes and indexes[s[i]]>=left:
                left = indexes[s[i]] + 1 # inc left by 1 of repeating character idx
            indexes[s[i]] = i
            max_len = max(max_len, i - left + 1)
        return max_len



            