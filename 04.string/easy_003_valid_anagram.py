# Problem: Determine whether two strings are anagrams of each other.
# Approach: Use a frequency array of size 26. Increment the count for
#           characters in s and decrement it for characters in t.
#           If all counts are zero, both strings contain the same
#           characters with the same frequencies.
# Time Complexity: O(n + m)
# Space Complexity: O(1) because the frequency array always has 26 elements.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        return all(count == 0 for count in freq)