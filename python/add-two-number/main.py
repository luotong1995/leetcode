from typing import Optional


# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = None
    r = None
    a = 0
    while True:
        if l1 and l2:
            sum = l1.val + l2.val + a
            a = sum // 10
            l1 = l1.next
            l2 = l2.next
            p = ListNode()
            p.val = sum % 10
            if result is None:
                result = p
                r = p
            else:
                r.next = p
                r = p
        elif (l1 and l2 is None):
            sum = l1.val + a
            a = sum // 10
            l1 = l1.next
            p = ListNode()
            p.val = sum % 10
            if result is None:
                result = p
                r = p
            else:
                r.next = p
                r = p
        elif (l2 and l1 is None):
            sum = l2.val + a
            a = sum // 10
            l2 = l2.next
            p = ListNode()
            p.val = sum % 10
            if result is None:
                result = p
                r = p
            else:
                r.next = p
                r = p
        else:
            if a != 0:
                p = ListNode()
                p.val = a
                if result is None:
                    result = p
                    r = p
                else:
                    r.next = p
                    r = p
            return result


if __name__ == '__main__':
    l = [2, 4, 5]

    a = None
    r = None
    for i in l:
        p = ListNode()
        p.val = i
        if a is None:
            a = p
            r = p
        else:
            r.next = p
            r = p

    l = [5, 6, 3]
    b = None
    r = None
    for i in l:
        p = ListNode()
        p.val = i
        if b is None:
            b = p
            r = p
        else:
            r.next = p
            r = p

    c = addTwoNumbers(a, b)
    print()
