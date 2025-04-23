# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k

        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        
        split_size = size // k
        remainder = size % k  

        current = head
        for i in range(k):
            ans[i] = current
            current_size = split_size + (1 if remainder > 0 else 0)
            remainder -= 1

            for _ in range(current_size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

        return ans
        