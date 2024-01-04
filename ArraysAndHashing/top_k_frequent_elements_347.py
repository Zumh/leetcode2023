"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency_table = {}
    """

    min_heap = []
    #result = []
    # find the frequency of each number
    for number in nums:
        frequency_table[number] = frequency_table.get(number, 0) + 1
    sorted_frequency = sorted(frequency_table.items(), key=lambda x: x[1], reverse=True)[:k]

    return [elem[0] for elem in sorted_frequency]
    """
    for number in nums: 
        frequency_table[number] = frequency_table.get(number, 0) + 1
    
    sorted_frequency = sorted(frequency_table.items(), key=lambda x: x[1], reverse=True)

    return [elem[0] for elem in sorted_frequency[:k]]


    
  
        
    

 

print(topKFrequent([1,1,1,2,2,3], 2))

print(topKFrequent([1], 1))