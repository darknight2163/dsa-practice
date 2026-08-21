class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Frequency map: count characters, then return the first one appearing once
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if freq[char] == 1:
                return i

        return -1