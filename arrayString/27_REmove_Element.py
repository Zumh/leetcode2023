"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Time Complexity

The provided code has a time complexity of O(n), where 'n' is the number of elements in the nums array. 
This is because the code iterates through each element of the array exactly once, and the number of iterations is directly proportional to the size of the array.

"""
def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):

        if nums[i] != val:
            # k is previous index
            # i is the current index
            nums[k] = nums[i]
            k +=1
    return k
nums = [3,2,2,3]
val = 3

val = removeElement(nums, val)

print(val)
