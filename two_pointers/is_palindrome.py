# Problem Link: https://leetcode.com/problems/valid-anagram/
# Submission Link: https://leetcode.com/problems/valid-anagram/submissions/1835588816/
# O(n) - no nested loops or sorting necessary
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join([char for char in s if char.isalnum()]).replace(' ', '').lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
