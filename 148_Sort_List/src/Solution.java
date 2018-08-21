
class Solution {
    // 使用归并排序的方法进行排序
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        // 将序列分成两部分
        ListNode pre = null;
        ListNode low = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            pre = low;
            low = low.next;
            fast = fast.next.next;
        }
        pre.next = null;

        ListNode l1 = sortList(head);
        ListNode l2 = sortList(low);
        return merge(l1, l2);
    }

    public ListNode merge(ListNode l1, ListNode l2) {
        ListNode new_head = null;
        ListNode r = null;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                if (new_head == null) {
                    new_head = l1;
                    r = new_head;
                } else {
                    r.next = l1;
                    r = l1;
                }
                l1 = l1.next;
            } else {
                if (new_head == null) {
                    new_head = l2;
                    r = new_head;
                } else {
                    r.next = l2;
                    r = l2;
                }
                l2 = l2.next;
            }
        }

        if (l1 != null) {
            r.next = l1;
        }
        if (l2 != null) {
            r.next = l2;
        }
        return new_head;
    }

    public static void main(String[] args) {
        ListNode head = null;
        ListNode r = null;
        int a[] = {6, 5, 3, 1, 9};
        for (int item : a) {
            ListNode node = new ListNode(item);
            if (head == null) {
                head = node;
                r = node;
            } else {
                r.next = node;
                r = node;
            }
        }
        r.next = null;
        Solution solution = new Solution();
        ListNode sort_head = solution.sortList(head);
        while(sort_head != null){
            System.out.println(sort_head.val);
            sort_head = sort_head.next;
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