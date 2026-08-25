# Problem: Group all anagrams together from a list of strings.
# Approach: Sort each string to create a common key. Anagrams produce
#           the same sorted string, so use a hash map to group strings
#           having the same key.
# Time Complexity: O(n * k log k), where n = number of strings and
#                  k = maximum length of a string.
# Space Complexity: O(n * k), for storing the grouped anagrams and keys.
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for s in strs:
            word = ''.join(sorted(s))
            if word not in mp:
                mp[word] = []
            mp[word].append(s)
        
        ans = []
        for k, v in mp.items():
            ans.append(v)

        return ans