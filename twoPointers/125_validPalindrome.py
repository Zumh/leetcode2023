def isPalindrome(self, s: str) -> bool:
        
        # extract only alphabets
        alphabets = [char for char in s if char.isalnum()]

        # lower all the characters
        lowerAlphabets = ''.join(alphabets).lower()

        if len(lowerAlphabets) == 0:
            return True
        # compare them from start and end.
        startIndex = 0
        endIndex = len(lowerAlphabets) - 1
        
        while startIndex < endIndex: 
            if lowerAlphabets[startIndex] != lowerAlphabets[endIndex]:
                return False
            startIndex+=1 
            endIndex-=1

        return True
