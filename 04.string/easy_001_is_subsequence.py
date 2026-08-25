# Problem: Check whether string s is a subsequence of string t.
# Approach: Use two pointers. Traverse t and move the pointer in s
#           whenever matching characters are found.
# Time Complexity: O(len(t))
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for t
        j = 0  # Pointer for s

        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == len(s)