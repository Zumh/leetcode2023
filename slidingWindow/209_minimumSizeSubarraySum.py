"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    left = 0

    min_length = float('inf')

    current_sum = 0

    for right in range(n):
        
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            # shrink the window from the left
            left += 1
    return min_length if min_length != float('inf') else 0

nums = [2,3,1,2,4,3]
target = 7
result = minSubArrayLen(target, nums)
print(result)
