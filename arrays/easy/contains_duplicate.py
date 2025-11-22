# Link: https://leetcode.com/problems/contains-duplicate
class Solution:

  # Initial solution https://leetcode.com/problems/contains-duplicate/submissions/1836400946/

  def containsDuplicate(self, nums: List[int]) -> bool:
    from collections import Counter

    seen = Counter(nums)

    if max(seen.values()) > 1:
      return True
    return False

    # After learning that sets remove duplicates, we can distill down
    # https://leetcode.com/problems/contains-duplicate/submissions/1836403504/
    def containsDuplicateOptimal(self, nums: List[int]) -> bool:
      return len(nums) != len(set(nums))
