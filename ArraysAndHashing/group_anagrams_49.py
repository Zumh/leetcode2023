"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # Time complexity O(n^2)
    # Space complexity O(n)
    result = []
    for word in strs: 
        for anagram  in result:

            # O(n) because letters start from a - z which is constant number 26 letters
            if isAnagram(word, anagram[0]):
                anagram.append(word)
                break
        else:
            result.append([word])
    return result
            
       
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

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

strs = [""]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))


# optimize solution

def groupAnagrams_optimize(strs: list[str]) -> list[list[str]]:
    # Time complexity O(n)
    # Space complexity O(n)
    result = {}
    for word in strs: 
        sorted_word = "".join(sorted(word))
        if sorted_word not in result:
            result[sorted_word] = [word]
        else:
            result[sorted_word].append(word)
    return list(result.values())
print("\n\noptimize solution\n\n")
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams_optimize(strs))

strs = [""]
print(groupAnagrams_optimize(strs))

strs = ["a"]
print(groupAnagrams_optimize(strs))