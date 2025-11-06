class Solution:
    def containsDuplicate(self, nums: list[int]):
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return True
            seen_numbers.add(num)
        return False
    
solution = Solution()

print(solution.containsDuplicate([1,3,5,9,11,24])) # False
print(solution.containsDuplicate([1,3,5,4,2,11,10,55,4,0])) # True