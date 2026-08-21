class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window + frequency map: check if any window matches s1's character frequencies
        from collections import Counter

        k = len(s1)
        if k > len(s2):
            return False

        freq1 = Counter(s1)
        window = Counter(s2[:k])

        if window == freq1:
            return True

        for right in range(k, len(s2)):
            window[s2[right]] += 1
            window[s2[right - k]] -= 1

            if window[s2[right - k]] == 0:
                del window[s2[right - k]]

            if window == freq1:
                return True

        return False