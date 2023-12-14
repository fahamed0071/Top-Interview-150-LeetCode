#https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1=""
        val2=""
        temp1=l1
        temp2=l2
        while temp1 is not None:
            val1 +=str(temp1.val)
            temp1=temp1.next
        while temp2 is not None:
            val2 +=str(temp2.val)
            temp2=temp2.next

        print("val1:{}".format(val1))
        print("val2:{}".format(val2))
        final_value=str(int(val1[::-1])+int(val2[::-1]))
        print("final_value:",final_value)

        l3=ListNode(final_value[0])
        self.head3=l3

        for i,val in enumerate(final_value):
            if i==0:
                continue
            new_node=ListNode(val)
            new_node.next=self.head3
            self.head3=new_node
        return self.head3




