"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""
def isSubsequence(self, s: str, t: str) -> bool:

        # keeping track of both index position can be use for order and matching character.

        subPointer = 0;
        strPointer = 0;

        while subPointer < len(s) and strPointer < len(t):

            if s[subPointer] == t[strPointer]:
                subPointer += 1
            strPointer += 1

        # making sure the final length is matched with sub string length
        return subPointer == len(s)
