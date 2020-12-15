# Time complexity: O(n^2); Space: O(1)
def twoNumberSum(array, target):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == target:
                return [firstNum, secondNum]
    return []


array = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 13
print(twoNumberSum(array, target))



