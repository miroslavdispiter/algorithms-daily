"""Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""

# uraditi bez ugnjezdenih for petlji...samo korsititi jednu

def threeSumClosest(nums, target):
    closestSum = float('inf')

    for i in range(len(nums)-2):
        for left in range(i+1, len(nums)):
            for right in range(left+1, len(nums)):
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(target - currentSum) < abs(target - closestSum):
                    closestSum = currentSum
                
                if currentSum == target:
                    return currentSum
    return closestSum

a = threeSumClosest([-1,2,1,-4], 1)
b = threeSumClosest([1,3,5,4,-4,9,2,8], 4)

print(a)
print(b)