"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
def summaryRanges(nums: list[int]) -> list[str]:
    if len(nums) == 1:
        return [f"{nums[0]}"]
    elif len(nums) == 0:
        return
    start = end = nums[0]
    pairRange = []
    for number in nums[1:]:

        # check the boundary for the range
        if end + 1 == number:
            # update the end
            end = number
        else:
            # we found ourselves a pair of range
            # if we have only one single number from the input list
            if start == end:
                pairRange.append(f"{start}")
            else:
                pairRange.append(f"{start}->{end}")
            # update start and end
            start = end = number
    # collecting the remaining data from nums
    if start == end:
        pairRange.append(f"{number}")
    else:
        pairRange.append(f"{start}->{end}")

    return(pairRange)

nums = [0,1,2,4,5,7]
result = summaryRanges(nums)
print(result)

