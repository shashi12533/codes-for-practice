def _toBST(self, head, tail):
    if head == tail:
        return None
    slow = fast = head
    while fast != tail and fast.next != tail:
        slow = slow.next
        fast = fast.next.next
    root = TreeNode(slow.val)
    root.left = self._toBST(head, slow)
    root.right = self._toBST(slow.next, tail)
    return root
