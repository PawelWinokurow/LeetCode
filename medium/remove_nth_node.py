from typing import Optional

from util.list_node import ListNode, create_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        fake = ListNode()
        fake.next = head
        fst = fake
        snd = fake
        while fst.next:
            if i < n:
                i += 1
            else:
                snd = snd.next
            fst = fst.next
        snd.next = snd.next.next
        return fake.next
