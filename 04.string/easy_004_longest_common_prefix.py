# Problem: Find the longest common prefix shared by all strings.
# Approach: The common prefix cannot be longer than the shortest string.
#           Compare each character of the shortest string with the same
#           position in every other string. Return immediately on mismatch.
# Time Complexity: O(n * m), where n = number of strings and
#                  m = length of the shortest string.
# Space Complexity: O(1), excluding the returned substring.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string
        shortest = min(strs, key=len)

        # Compare each character with all strings
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]

        return shortest