# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def list2bst(head):
            if not head:
                return 
            left = head 
            mid = right = left 
            prev = None
            while right and right.next:
                prev = mid
                mid = mid.next
                right = right.next.next 
            if not prev:
                return TreeNode(head.val)
            prev.next = None 
            return TreeNode(mid.val, left = list2bst(left), right = list2bst(mid.next))
        return list2bst(head)
