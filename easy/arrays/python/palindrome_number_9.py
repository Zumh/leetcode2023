"""
Given an integer x, return true if x is a

, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

"""

def isPalindrome(x: int)->bool:
    status = False
    if x < 0:
        return status

    original = x
    reverse = 0
    
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    return original == reverse
status = isPalindrome(121)
print(status)
