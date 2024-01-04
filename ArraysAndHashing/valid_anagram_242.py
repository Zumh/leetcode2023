"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
"""

# brute force solution

def isAnagram(s: str, t: str) -> bool:
    anagram_status = True
    # check the length if not the same then return false
    # 61 ms Time Complexity O(n)
    if len(s) != len(t):
        anagram_status = False
    else:
        # here we going to compare each character
        # we can use dictionary for this
        # in the essence we are loooking for same latter from each string
        unique_letters = {}
        for letter in s:
            if letter not in unique_letters:
                unique_letters[letter] = 1
            else:
                unique_letters[letter] += 1
        for letter in t:
            if unique_letters.get(letter, 0) == 0:
                anagram_status = False
                break
            else:
                unique_letters[letter] -= 1
                if unique_letters[letter] == 0:
                    unique_letters.pop(letter)
            
        
    return anagram_status


s = "anagram"
t = "nagaram"
print(isAnagram(s, t)) 
s = "rat"
t = "car"
print(isAnagram(s, t)) 