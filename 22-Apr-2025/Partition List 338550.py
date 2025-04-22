# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, r = ListNode(), ListNode()
        ltail, rtail = l, r

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next =head
                rtail = rtail.next
            head = head.next
        ltail.next = r.next
        rtail.next = None
        return l.next
        