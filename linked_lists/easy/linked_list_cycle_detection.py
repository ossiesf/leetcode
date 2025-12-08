# Initial solution while O(n) was not optimal
# For the second solution, I implemented Floyd's Cycle Detection Algorithm

# Submission 1: https://leetcode.com/problems/linked-list-cycle/submissions/1849756135/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        current = head
        index = 0
        while current:
            if current not in seen:
                seen[current] = index
            else: return True
            current = current.next
        return False

# Solutuion 2 (Floyd's Cycle Detection): https://leetcode.com/problems/linked-list-cycle/submissions/1849765483/
# Uses two pointers, and the technique ensures eventually they will meet if there is a cycle
  class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
