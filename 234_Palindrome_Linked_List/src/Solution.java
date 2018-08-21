
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }
        int length = 0;
        ListNode cur = head;
        while (cur != null) {
            length++;
            cur = cur.next;
        }

        if (length == 1) {
            return true;
        }
        ListNode mid = null;
        cur = head;
        mid = cur;
        while (cur.next != null && cur.next.next != null) {
            mid = mid.next;
            cur = cur.next.next;
        }
        ListNode right = mid.next;
        ListNode new_head = reverse(right);
        mid.next = null;
        ListNode l = head;
        ListNode r = new_head;
        while (l != null && r != null) {
            if (l.val != r.val) {
                return false;
            }
            l = l.next;
            r = r.next;
        }
        return true;
    }

    public ListNode reverse(ListNode head) {
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


    public void print(ListNode head) {
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }

    public static void main(String[] args) {
        int a[] = {1, 2};
        ListNode head = null;
        ListNode r = null;
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
        Solution solution = new Solution();
        System.out.println(solution.isPalindrome(head));
    }
}


class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}