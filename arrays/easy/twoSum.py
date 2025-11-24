# Problem: https://leetcode.com/problems/two-sum/
# Solution is O(n) - this differs from earlier hashmap problems in that instead of counting
# We are storing the index as the value with the number value as the key
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in seen:
                return [seen[remainder], i]
            seen[nums[i]] = i
                
        return []
