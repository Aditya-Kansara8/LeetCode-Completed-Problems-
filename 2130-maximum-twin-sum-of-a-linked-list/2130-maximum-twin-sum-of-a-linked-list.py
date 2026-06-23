# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        d = deque()
        s = 0
        current = head
        while current:
            d.append(current.val)
            current = current.next
        while d:
            t = d.popleft() + d.pop()
            if t > s:
                s = t
        return s