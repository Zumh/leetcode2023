"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate_brute():
    # Time complexity O(n^2)
    # Space complexity O(1)
    # Assuming we have at least two element in array.
    #nums = [1,2,3,1]
    nums = [1,1,1,3,3,4,3,2,4,2]
    #nums = [1,2,3,4]
    duplicate_status = False
    count_duplicate = 1
    # change status from False to true

    selected_index = 0
    next_index = 1
    while (next_index < len(nums)):
        if count_duplicate == 2:
            duplicate_status = True
            break
        # compare selected element and the rest of the number for possible duplicate
        if nums[selected_index] == nums[next_index]:
            count_duplicate += 1
        next_index += 1
        # reset varaibles for the next search in duplicated number
        if next_index == len(nums) - 1 and count_duplicate < 2:
            count_duplicate = 1
            selected_index += 1
            next_index = selected_index + 1
    return duplicate_status
    

  
    
def containsDuplicate_optimize():
    # memmory complexity O(n)
    # time complexity O(n) 427
    # Time exceeded and doesn't work
    #nums = [1,2,3,1]
    #nums = [1,1,1,3,3,4,3,2,4,2]
    nums = [1,2,3,4]

    # we going to store numbers that are unique
    unique_nums = set()
    duplicate_status = False
    for num in nums:
        # because of set data structure we are able to check element in set ds in O(1)
        if num not in unique_nums:
            unique_nums.add(num)
        else: 
            duplicate_status = True
            break
    return duplicate_status


# sort them first and then check if the next number is equal to the previous one
# pass by 495 ms
def containsDuplicate_sort():
    # time complexity O(nlogn) because of sorted algorithm
    nums = [1,2,3,1]
    #nums = [1,1,1,3,3,4,3,2,4,2]
    #nums = [1,2,3,4]

    # sort nums 
    sorted_nums = sorted(nums)
    # duplicated satus code 
    duplicated_status = False
    current_num = 0
    next_num = 1
    while next_num < len(sorted_nums):
        if sorted_nums[current_num] == sorted_nums[next_num]:
            duplicated_status = True
            break
        current_num += 1
        next_num += 1
    return duplicated_status

def containsDuplicate_dict():
    # 439 ms Time Complexity O(n)
    # Space Complexity O(n)
    #nums = [1,2,3,1]
    #nums = [1,1,1,3,3,4,3,2,4,2]
    nums = [1,2,3,4]
    frequency_table = {}
    duplicate_status = False
    frequency_count = 0
    for num in nums:
        
        # get the frequency of a number if exist otherwise increment by 1
        frequency_count = frequency_table.get(num, 0)
        frequency_table[num] = frequency_count + 1

        if frequency_table[num] >= 2:
            duplicate_status = True
            break

    return duplicate_status

#print(containsDuplicate_brute())
#print(containsDuplicate_optimize()) # failed
#print(containsDuplicate_sort())
print(containsDuplicate_dict())