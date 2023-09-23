class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueCounter = 1
        counter = 1
        if nums[index] != nums[index - 1]:
            nums[unqiueCounter] = nums[index]
            if counter >= 2:
                uniqueCounter += 1

            counter = 0
        else:
            counter += 1
        
