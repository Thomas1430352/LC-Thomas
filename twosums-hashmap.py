from typing import List

#hashmap for two sum solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
nums = [2,7,11,15]
target = 22
solution = Solution()
result = solution.twoSum(nums, target)
print (result)