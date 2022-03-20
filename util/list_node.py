from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=', ')
        head = head.next

def create_list(list: List):
    list_reversed = list[::-1]
    fake_head = ListNode()
    prev = fake_head
    for el in list_reversed:
        tail = ListNode(el)
        prev.next = tail
        prev = tail
    return fake_head.next