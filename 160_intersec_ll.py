# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1, list2 = headA,headB
        while list1 != list2:
           list1 = list1.next if list1 else headB
           list2 = list2.next if list2 else headA
            # if list1:
            #     list1 = list1.next
            # else:
            #     list1 = headB
            #
            # if list2:
            #     list2 = list2.next
            # else:
            #     list2 = headA
        return list1