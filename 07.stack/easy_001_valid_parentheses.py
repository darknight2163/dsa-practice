# Problem: Check whether a string containing brackets is valid.
# Approach: Use a stack to store opening brackets. For every closing
#           bracket, check whether it matches the most recent opening
#           bracket.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            else:
                if not stack:
                    return False

                top = stack.pop()

                if (ch == ')' and top != '(') or \
                   (ch == '}' and top != '{') or \
                   (ch == ']' and top != '['):
                    return False

        return len(stack) == 0