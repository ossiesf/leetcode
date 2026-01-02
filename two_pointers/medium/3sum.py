# Initial draft solution, does not pass all test cases yet
# Link: https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size < 3:
            return []
        result = []

        # Sort the array so that we know if each index move makes
        # The total bigger or smaller so we can approach 0
        nums.sort()
        for i in range(size - 2):
            j = i+1
            k = size - 1
            total = 1

            while total != 0 and j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:
                        result.append(triplet)
                    j+=1
                    k-=1
                if total > 0:
                    k-=1
                if total < 0:
                    j+=1

        return result
