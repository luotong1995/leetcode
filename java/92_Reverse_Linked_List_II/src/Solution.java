import java.util.Stack;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {

    public ListNode reverseBetween(ListNode head, int m, int n) {
        Stack<ListNode> stack = new Stack<>();
        if (head == null || head.next == null) {
            return head;
        }
        int count = 1;
        ListNode cur = head;
        ListNode l = null;
        ListNode r = null;

        while (cur != null) {
            if (count == m - 1) {
                l = cur;
            }
            if (count == n + 1) {
                r = cur;
            }
            if (count >= m && count <= n) {
                stack.push(cur);
            }
            cur = cur.next;
            count++;
        }
        ListNode temp = null;
        while (!stack.isEmpty()) {
            if (l != null) {
                temp = stack.pop();
                l.next = temp;
                l = temp;
            } else {
                temp = stack.pop();
                l = temp;
                if (m == 1) {
                    head = l;
                }
            }
        }
        l.next = r;
        return head;
    }

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

    public void print(ListNode head) {
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }

    public static void main(String[] args) {
        int a[] = {1, 2, 3, 4};
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
        solution.print(solution.reverseBetween(head, 1, 2));
    }
}