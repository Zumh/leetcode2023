"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
def canConstruct(ransomNote: str, magazine: str) -> bool:
    # count the frequency of all the letters from magazine
    frequency = {}

    for letter in magazine:
        frequency[letter] = frequency.get(letter, 0) + 1

    # start decrementing and check if the ransomeNote and magazine frequency match
    for letter in ransomNote:
        if letter in frequency and frequency[letter] > 0:
            frequency[letter] -= 1
        else:
            return False
    return True
ransomNote = "a"
magazine = "b"
result = canConstruct(ransomNote, magazine) 
print(result)

