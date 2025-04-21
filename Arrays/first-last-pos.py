"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
# Made with time complexity O(n), tommorow I will try to make with
# time complexity O(log n). Idea: Binary search

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

nums = [5,7,7,8,8,8,8,10]
target = 7
print(posFirstLast(nums, target))
nums = []
target = 0
print(posFirstLast(nums, target))