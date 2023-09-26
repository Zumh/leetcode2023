# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums: list[int]) -> int:
        uniqueValueIndex = 1
        for index in range(1, len(nums)):

            if nums[index] != nums[index - 1]:
                    nums[uniqueValueIndex] = nums[index] 
                    uniqueValueIndex += 1
        return uniqueValueIndex
unique = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(unique)
