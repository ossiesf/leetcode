# Solution is O(n) since each element is pushed once only
# Problem link: https://leetcode.com/problems/daily-temperatures/submissions/1866996417/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = []
        results = [0] * len(temperatures)
        index = 0

        for i in range(len(temperatures)):
            while indices and temperatures[i] > temperatures[indices[-1]]:
                prev_idx = indices.pop()
                results[prev_idx] = i - prev_idx
            indices.append(i)
        return results
