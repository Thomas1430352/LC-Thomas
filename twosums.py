from typing import List

#two sum solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target: 
                         return([i, j])
                    
nums = [2,7,11,15]
target = 22
solution = Solution()
result = solution.twoSum(nums, target)
print (result)