def twoNumberSum(array, target):
    nums = {}
    for num in array:
        potentialMatch = target - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


array = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 13
print(twoNumberSum(array, target))
