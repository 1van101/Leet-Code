# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        vals = []
        curr_node = head

        while curr_node is not None:
            vals.append(curr_node)
            curr_node = curr_node.next

        mid = len(vals) // 2

        return vals[mid]
