# Problem: Find the first bad version when all versions after it are
#          also bad.
# Approach: Use binary search. If mid is bad, the first bad version is
#           at mid or to its left. If mid is good, the first bad version
#           must be to its right.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low