#! /usr/bin/python3

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

- Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""


"""
Time complexity

O(m + n)

In the first part of the function, we use two pointers p1 and p2 to iterate through both arrays from the end to the beginning. In the worst case, we need to iterate through all elements in both nums1 and nums2, which gives us a time complexity of O(m + n) for this part.

In the second part of the function, if there are any remaining elements in nums2, we add them to nums1. Since we only iterate through the remaining elements in nums2, the time complexity of this part is O(n).

Overall, the time complexity of the entire function is O(m + n) due to the dominating part in the first step.
"""
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize three pointers: 'p1, p2, p' to point to the last valid elements in nums1, nums2, and the last position in the merged array, respectively.
        
        p1, p2, p = m - 1, n - 1, m + n - 1

        # compare the elements at nums1[p1] and nums2[p2]. 
        # Start from the end of the arrays and move towards the beginning.
        while p1 >= 0 and p2 >= 0:
            # Compare the elements, and put the greater one at nums1[p1].
            # Decrement p accordingly and move the corresponding pointer
            # (p1 or p2) one step back.
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
            # Repeat this process until all elements from both arrays have been merged into nums1

        # If there are any remaining elements in nums2, add them to nums1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -=1 
            p -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(nums1)
merge(nums1, m, nums2, n)
print(nums1)
