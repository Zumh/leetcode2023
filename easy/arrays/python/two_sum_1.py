def twoSum(nums: list[int], target: int):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    
    difference + numberInArray = target

    difference = target - numberInArray
   
    if commonDifference not found in array
        
        store unique differen and index
        [difference] = index
    
    else
        
        otherwise return indexes found
        result = [[difference], currentIndex]

    is the difference exists if not add in the dictionary

    """
    differences = {}
    result = []
    for index, current_number in enumerate(nums):
        current_difference = target - current_number
        if current_difference in differences:

            result.append([differences[current_difference], index])
            
            return result
        # if no common differences then store current number with their index
        # this is same as eliminating possible number
        differences[current_number] = index 
    return result 

result = twoSum([2,7,11,15], 9)

print(result)
    
