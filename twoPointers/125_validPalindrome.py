"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
def isPalindrome(self, s: str) -> bool:
        
    modified_s = ''.join(c for c in s if c.isalnum()).lower()
        
    # Compare characters from both ends
    left, right = 0, len(modified_s) - 1
    while left < right:
        if modified_s[left] != modified_s[right]:
            return False
        left += 1
        right -= 1
    return True





















