class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode new_node = null;
        ListNode r = null;
        if (l1 == null && l2 == null) {
            return null;
        }
        while (l1 != null && l2 != null) {
            ListNode next_1 = l1.next;
            ListNode next_2 = l2.next;
            if (l1.val <= l2.val) {
                if (new_node == null) {
                    new_node = l1;
                    r = l1;
                } else {
                    r.next = l1;
                    r = l1;
                }
                l1 = next_1;
            } else {
                if (new_node == null) {
                    new_node = l2;
                    r = l2;
                } else {
                    r.next = l2;
                    r = l2;
                }
                l2 = next_2;
            }
        }
        if (l1 == null) {
            if (new_node == null) {
                new_node = l2;
                r = l2;
            } else {
                r.next = l2;
                r = l2;
            }
        }
        if (l2 == null) {
            if (new_node == null) {
                new_node = l1;
                r = l1;
            } else {
                r.next = l1;
                r = l1;
            }
        }
        return new_node;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode head1 = null;
        int a[] = {1, 2, 3, 4, 5, 6, 7};
        ListNode r = null;
        for (int i = 0; i < a.length; i++) {
            ListNode node = new ListNode(a[i]);
            if (head1 == null) {
                head1 = node;
                r = node;
            } else {
                r.next = node;
                r = node;
            }
        }
        r.next = null;
        ListNode head2 = null;
        int b[] = {0, 1, 2, 3, 4, 5, 7, 8, 12};
        r = null;
        for (int i = 0; i < b.length; i++) {
            ListNode node = new ListNode(b[i]);
            if (head2 == null) {
                head2 = node;
                r = node;
            } else {
                r.next = node;
                r = node;
            }
        }
        r.next = null;
        ListNode new_head = solution.mergeTwoLists(head1, head2);
        while (new_head != null) {
            System.out.println(new_head.val);
            new_head = new_head.next;
        }

    }
}


class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}
