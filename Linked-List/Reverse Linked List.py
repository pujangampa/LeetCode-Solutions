class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newlist=None
        curr=head
        while curr:
             nextnode=curr.next
             curr.next=newlist
             newlist=curr
             curr=nextnode
        return newlist
