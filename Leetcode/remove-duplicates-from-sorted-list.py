# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    # ListNode -> ListNode
    def deleteDuplicates(self, head, result=None, last_added=None, ptr=None):
        if head == None:
            return ptr
        else:
            if head.val == last_added:
                return self.deleteDuplicates(head.next, result, last_added, ptr)
            else:
                if result == None:
                    result = ListNode(head.val, last_added)
                    return self.deleteDuplicates(head.next, result, head.val, result)
                else:
                    result.next = ListNode(head.val, None)
                    return self.deleteDuplicates(head.next, result.next, head.val, ptr)
