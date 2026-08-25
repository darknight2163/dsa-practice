# Problem: For every number from 0 to n, return the number of 1s
#          in its binary representation.
# Approach: Start with [0]. Each new range of numbers can be generated
#           by taking the existing values and adding 1 to each count.
#           Continue extending the array until it contains n + 1 values.
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]

        while len(output) <= n:
            output.extend([a + 1 for a in output])

        return output[:n + 1]