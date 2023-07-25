class Solution:
    def getIntersectionNode(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:
        st=set()
        while (h1!=None):
            st.add(h1)
            h1=h1.next
        while (h2!=None):
            if h2 in st:
                return h2
            h2=h2.next
        return None
