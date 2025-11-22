class Solution:

  # Initial solution
  def containsDuplicate(self, nums: List[int]) -> bool:
    from collections import Counter

    seen = Counter(nums)

    if max(seen.values()) > 1:
      return True
    return False

    # After learning that sets remove duplicates, we can distill down to:
    def containsDuplicateOptimal(self, nums: List[int]) -> bool:
      return len(nums) != len(set(nums))
