# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list3 = None
    p = None
    while list1 or list2:
        if list1 and list2:
            if list1.val < list2.val:
                if list3 is None:
                    list3 = ListNode(val=list1.val)
                    p = list3
                else:
                    r = ListNode(val=list1.val)
                    p.next = r
                    p = r
                list1 = list1.next
            else:
                if list3 is None:
                    list3 = ListNode(val=list2.val)
                    p = list3
                else:
                    r = ListNode(val=list2.val)
                    p.next = r
                    p = r
                list2 = list2.next
        elif list1:
            if list3 is None:
                list3 = ListNode(val=list1.val)
                p = list3
            else:
                r = ListNode(val=list1.val)
                p.next = r
                p = r
            list1 = list1.next
        elif list2:
            if list3 is None:
                list3 = ListNode(val=list2.val)
                p = list3
            else:
                r = ListNode(val=list2.val)
                p.next = r
                p = r
            list2 = list2.next
    return list3


def print_list(l):
    while l:
        print(l.val)
        l = l.next


if __name__ == '__main__':
    # init list1
    l1 = []
    list1 = None
    p = None
    for item in l1:
        if list1 is None:
            list1 = ListNode(val=item)
            p = list1
        else:
            r = ListNode(val=item)
            p.next = r
            p = r
    # print_list(list1)
    # init list2
    l2 = []
    list2 = None
    p = None
    for item in l2:
        if list2 is None:
            list2 = ListNode(val=item)
            p = list2
        else:
            r = ListNode(val=item)
            p.next = r
            p = r
    # print_list(list2)
    print_list(mergeTwoLists(list1, list2))
