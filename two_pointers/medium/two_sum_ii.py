# O(n) solution for a sorted array
# Problem link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1862971665/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left+1, right+1]
            elif result > target:
                right -= 1
            else:
                left += 1
        return []
