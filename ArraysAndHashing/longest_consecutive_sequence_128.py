"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
> [1,2,3,4,100,200] > [1,2,3,4] [100] [200]

Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

def longestConsecutive(nums: list[int]) -> int:
    
    longest_length = 0
    # this number set is used for base 
    nums_set = set(nums)
    # traverse through the array and check the difference of 1 in array
    for num in nums:

        # if number - 1 is not in array then it is the start of the sequence
        if num - 1 not in nums_set: 
            length = 1
            # num + 1 is in nums set it mean we have a sequence and difference is + 1
            while num + 1 in nums_set:
                length += 1
                num += 1
            # update the longest length
            longest_length = max(length, longest_length)

    return longest_length

nums = [100,4,200,1,3,2]

print(longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]

print(longestConsecutive(nums))