# Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Submission Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1843178217/
# Complexity of O(1) - iterating over the hashset rather than the array avoids checking duplicate values
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        streak = 0
        seen = set(nums)
        
        for n in seen:
            if (n - 1) not in seen:
                # Start the chain
                streak += 1
                i = 1
                while True:
                    if (n+i) in seen:
                        streak += 1
                        i += 1
                    else:
                        break
                    
                if streak > longest:
                    longest = streak
                streak = 0
                
        return longest
