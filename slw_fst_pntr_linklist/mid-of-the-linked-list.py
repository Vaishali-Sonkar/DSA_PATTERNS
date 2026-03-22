# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow=fast=head                  #set both slow and fast pointers to the head of the linked list initially
        while fast and fast.next:     #while the fast pointer is not null and the next node of the fast pointer is not null, we can continue moving the pointers
            slow=slow.next        #move the slow pointer one step forward (to the next node)
            fast=fast.next.next   #move the fast pointer two steps forward (to the next of the next node)
        return slow                #when the fast pointer reaches the end of the linked list (either it becomes null or its next node becomes null), the slow pointer will be at the middle node of the linked list, so we return the slow pointer as the result.