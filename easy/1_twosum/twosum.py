'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
'''

def twoSum( nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]   

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
'''

def two_sum(nums, target):
    # key: num, value: index
    num_to_index = {}  # Initialize the hash map

    for index, num in enumerate(nums):
        # 9 - 2 = 7
        complement = target - num  # Calculate the complement
        
        if complement in num_to_index:
            # If complement is found, return the indices
            return [num_to_index[complement], index]
        
        # Otherwise, add the number and its index to the hash map
        num_to_index[num] = index

    # Since the problem guarantees one solution, we do not need to handle the case of not finding a solution
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))