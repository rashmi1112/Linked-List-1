class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reversed_head
