# Problem: Reverse the order of words in a string while keeping
#          exactly one space between consecutive words.
# Approach: Split the string into words, reverse the list using
#           two-pointer swapping, and join the words with spaces.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        # Reverse the list using two pointers
        left = 0
        right = len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return ' '.join(words)