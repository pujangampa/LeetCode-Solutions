class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if (fast==slow):
                return True
        return False
