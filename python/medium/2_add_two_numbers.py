# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ''
        l2_str = ''

        l1_current_node = l1

        while l1_current_node is not None:
            l1_str += str(l1_current_node.val)
            l1_current_node = l1_current_node.next

        l2_current_node = l2

        while l2_current_node is not None:
            l2_str += str(l2_current_node.val)
            l2_current_node = l2_current_node.next

        result = str(int(l1_str[::-1]) + int(l2_str[::-1]))[::-1]

        final = ListNode(0)
        tmp = final

        for i in result:
            tmp.next = ListNode(int(i))
            tmp = tmp.next

        return final.next




