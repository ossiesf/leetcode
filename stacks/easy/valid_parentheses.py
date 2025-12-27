# O(n) solution
# Problem link: https://leetcode.com/problems/valid-parentheses/submissions/1835548447/
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "[": "]", "{": "}"}

        seen = []
        result = 1
        
        if len(s) % 2 != 0:
            return False
        if len(s) > 1:
            for char in s:
                # Check to see if it's an open or close
                # If it's an open, add to stack
                if char in brackets.keys():
                    seen.append(char)
                elif char in brackets.values():
                    # If you see a close, check that you still have an open for it
                    # If you get a close of type A right next to a close of b,
                    # This fails
                    if not seen or char != brackets[seen[-1]]:
                        return False
                    # Remove if matched
                    else:
                        seen.pop()
        else:
            return False
        
        # If the stack isn't empty, return False
        return len(seen) == 0
