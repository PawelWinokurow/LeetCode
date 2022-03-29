from typing import Optional

from util.list_node import ListNode, create_list


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode()
        if head:
            fake.next = head
        node = fake
        while node.next and node.next.next:
            fst = node.next
            snd = node.next.next
            third = node.next.next.next
            node.next = snd
            snd.next = fst
            fst.next = third
            node = fst
        return fake.next


sol = Solution()
head = create_list([1])
ret = sol.swapPairs(head)
pass