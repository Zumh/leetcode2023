"""
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = 2
        # return if length is less than 3
        if len(nums) <= freq:
            return len(nums)

        # calculate the duplicate of 2 number
        minIndex = freq
        maxIndex = freq

        while maxIndex < len(nums):
            # remember the right one will be 
            # we found number to replace for the third value from the list
            maxValue = nums[maxIndex]
            minValue = nums[minIndex - freq]
            if minValue != maxValue:
                # we replace the third position with unique maxValue
                nums[minIndex] = maxValue

                # minIndex by one
                minIndex += 1
            
            maxIndex += 1
        
        return minIndex

