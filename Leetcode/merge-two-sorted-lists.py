class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2      
