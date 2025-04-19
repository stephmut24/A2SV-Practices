# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        curr = head
        for i in range(length -k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next  = None
        tail.next = head

        return newHead