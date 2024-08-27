from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    re = None
    b = 0
    a = 0
    r = None
    while l1 and l2:
        sum = l1.val + l2.val + b
        a = sum % 10
        b = sum // 10
        p = ListNode(a)
        if re is None:
            re = p
            r = p
        else:
            r.next = p
            r = p
        l1 = l1.next
        l2 = l2.next

    while l1:
        sum = l1.val + b
        a = sum % 10
        b = sum // 10
        p = ListNode(a)
        if re is None:
            re = p
            r = p
        else:
            r.next = p
            r = p
        l1 = l1.next

    while l2:
        sum = l2.val + b
        a = sum % 10
        b = sum // 10
        p = ListNode(a)
        if re is None:
            re = p
            r = p
        else:
            r.next = p
            r = p
        l2 = l2.next

    if b != 0:
        r.next = ListNode(b)

    return re


a = None
r = None
for item in [2, 4, 3]:
    p = ListNode(item)
    if a is None:
        a = p
        r = p
    else:
        r.next = p
        r = p

b = None
r = None
for item in [5, 6, 4]:
    p = ListNode(item)
    if b is None:
        b = p
        r = p
    else:
        r.next = p
        r = p
