class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode new_head = null;
        ListNode next = null;
        while (head != null) {
            next = head.next;
            head.next = new_head;
            new_head = head;
            head = next;
        }
        return new_head;
    }
}