# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or  not head.next:
            return head
        slow=head
        fast=head.next 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid =slow.next
        slow.next=None
        left=self.sortList(head)  
        right=self.sortList(mid)   
        return self.merge(left,right)

    def merge(self,l,r):
        dummy=ListNode(0)
        tail=dummy
        while l and r:

            if l.val < r.val:
                tail.next=l
                l=l.next
            else:
                tail.next=r
                r =r.next
            tail=tail.next    
        if l:
            tail.next=l
        if r:
            tail.next=r
        return dummy.next                      