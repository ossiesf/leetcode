# This is not an efficient solution, O(n^2)
# Results in a timeout if nums is too large
# TODO: New solution with complexity < n^2
# Problem link: https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        for i in range(length):
            for j in range(length):
                if j is not i:
                    if nums[j] == 0:
                        result[i] = 0
                        break
                    elif result[i] == 0:
                        result[i] += 1 * nums[j]
                    else:
                        result[i] = result[i] * nums[j]
        return result
