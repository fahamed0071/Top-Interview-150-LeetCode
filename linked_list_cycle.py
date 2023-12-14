#https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer=head
        slow_pointer=head
        while slow_pointer !=None and fast_pointer!=None and fast_pointer.next!=None:
            slow_pointer =slow_pointer.next
            fast_pointer=fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False