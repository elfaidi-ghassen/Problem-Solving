class Solution(object):
    def reverseList(self, head):
        def reverseList0(head, acc):
            if head == None:
                return acc
            else:
                return reverseList0(head.next, ListNode(head.val, acc))
        
        return reverseList0(head, None)
