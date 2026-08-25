# Problem: Check whether a string is a palindrome after considering
#          only alphanumeric characters and ignoring case.
# Approach: Use two pointers from both ends. Skip non-alphanumeric
#           characters and compare valid characters.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "0123456789abcdefghijklmnopqrstuvwxyz"
        i=0
        j=len(s)-1
        while i<j:
            # Skip non-alphanumeric characters from the left
            if s[i].lower() not in valid:
                i+=1
                continue
            # Skip non-alphanumeric characters from the right
            if s[j].lower() not in valid:
                j-=1
                continue
            # Compare characters ignoring case
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
            
        