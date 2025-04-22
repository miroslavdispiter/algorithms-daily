"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
# Made with time complexity O(n), linear search.
"""
def posFirstLast(nums, target):
    pos1 = -1
    pos2 = -1
    counter = 0

    for i in range(len(nums)):
        if nums[i] == target and counter == 0:
            pos1 = i
            counter += 1
        elif nums[i] == target and counter == 1:
            pos2 = i
    return [pos1, pos2]
"""
# Made with time complexity O(log(n)), binary search.

def binarySearch(nums, target, findFirst):
    left = 0
    right = len(nums)-1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid

            if findFirst:
                right = mid - 1  # nastavljamo traziti levo
            else:
                left = mid + 1  # nastavljamo traziti desno
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
 
def posFirstLast(nums, target):
    first = binarySearch(nums, target, True)
    last = binarySearch(nums, target, False)
    return [first, last]

nums = [5,7,7,7,8,8,8,8,10]
target = 7
print(posFirstLast(nums, target))

nums = []
target = 0
print(posFirstLast(nums, target))