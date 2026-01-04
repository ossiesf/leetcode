# Link: https://leetcode.com/problems/3sum/
# Second solution, this one with checks for dupes and avoid checking
# If 'triplets' in result as this is expensive
# See comments for changes
# Solution is O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        k = size-1
        result = []

        nums = sorted(nums)

        for i in range(size-2):
            # Check for dupes of i
            # If dupe, go to next iteration of for loop
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])

                    # Check / skip duplicates for j & k
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1

                    # Since the list is sorted, if we find a match
                    # Increment j: we are gauranteed to be > 0 for all other values of j
                    # Decrement k to balance that out
                    j+=1
                    k-=1
            k = size-1
        return result

# Initial draft solution, does not pass all test cases yet
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
