# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        list1.reverse()
        list2.reverse()
        list1 = [str(num) for num in list1]
        list2 = [str(num) for num in list2]
        list1 = ''.join(list1)
        list2 = ''.join(list2)

        list1 = int(list1)
        list2 = int(list2)
        result = str(list1+list2)
        resultList = []
        for num in result:
            resultList.append(int(num))

        dummy = None
        for num in resultList:
            dummy = ListNode(num, dummy)
        return dummy