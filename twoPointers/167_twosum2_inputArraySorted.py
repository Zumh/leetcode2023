def twoSum(numbers: list[int], target: int) -> list[int]:
    
    leftPointer = 0
    rightPointer = len(numbers) - 1
    totalSum = numbers[0]
    temp = target
    while leftPointer < rightPointer:

        # traverse through all the left
        # first value from the right side of sorted array
        while temp < numbers[rightPointer]:
            rightPointer -= 1

        # temp is the left side of target value or second value
        temp = target - numbers[rightPointer]

        # we increment the index all the way from the left till temp value is equal to the numbers we can find in array
        while temp > numbers[leftPointer]:
            leftPointer += 1
        
        if target == numbers[leftPointer] + numbers[rightPointer]:

            return [leftPointer + 1, rightPointer + 1]
    return []

numbers = [2, 7, 11, 15]
target = 9

print(twoSum(numbers, 9))
