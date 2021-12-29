from typing import Optional

from util.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head:
            next = head.next
            head.next = last
            last = head
            head = next
        return last
