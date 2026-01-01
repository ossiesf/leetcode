# Second solution, O(n)
# Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1871407523/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and suffix approach
        # First calculate for each index 'product of everything before me'
        # Then calc 'product of everything after me'
        # Then multiply the results
        size = len(nums)

        prefix = [0] * size
        running_total = 1
        for i in range(size):
            # Save current total before creating new product
            # As to exclude the current index in the calculation
            prefix[i] = running_total
            running_total = nums[i] * running_total

        suffix = [0] * size
        running_total = 1
        for i in range(size - 1, -1, -1):
            suffix[i] = running_total
            running_total = nums[i] * running_total

        for i in range(size):
            nums[i] = prefix[i] * suffix[i]

        return nums

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
                if j != i:
                    if nums[j] == 0:
                        result[i] = 0
                        break
                    elif result[i] == 0:
                        result[i] += 1 * nums[j]
                    else:
                        result[i] = result[i] * nums[j]
        return result
