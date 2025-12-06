# Problem Link: https://leetcode.com/problems/reverse-linked-list
# Submission link: https://leetcode.com/problems/reverse-linked-list/submissions/1848010845/
# Complexity is O(n) - creates a second linked list while consuming the first
# Avoids traversing the chain more than once

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# head = [0,1,2,3]

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
