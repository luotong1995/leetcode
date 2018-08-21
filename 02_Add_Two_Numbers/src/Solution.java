import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int ca = 0;
        ListNode l3 = null;
        ListNode r = null;

        while(l1 != null && l2 !=null){
            int a = l1.val;
            int b = l2.val;
            int c = a + b + ca;
            ca = c / 10;
            c = c % 10;
            ListNode p = new ListNode(c);
            if(l3 == null){
                l3 = p;
                r = p;
                p.next = null;
            }else{
                r.next = p;
                r = p;
            }
            l1 = l1.next;
            l2 = l2.next;
        }

        while(l1 == null && l2 !=null){
            int b = l2.val;
            int c =  b + ca;
            ca = c / 10;
            c = c % 10;
            ListNode p = new ListNode(c);
            if(l3 == null){
                l3 = p;
                r = p;
                p.next = null;
            }else{
                r.next = p;
                r = p;
            }
            l2 = l2.next;
        }

        while(l1 != null && l2 ==null){
            int b = l1.val;
            int c =  b + ca;
            ca = c / 10;
            c = c % 10;
            ListNode p = new ListNode(c);
            if(l3 == null){
                l3 = p;
                r = p;
                p.next = null;
            }else{
                r.next = p;
                r = p;
            }
            l1 = l1.next;
        }

        if(ca != 0){
            ListNode p = new ListNode(ca);
            if(l3 == null){
                l3 = p;
                r = p;
                p.next = null;
            }else{
                r.next = p;
                r = p;
            }
        }
        return l3;
    }


    public static void print_list(ListNode L){
        ListNode l2 = L;
        while(l2 != null){
            System.out.print(l2.val);
            l2 = l2.next;
        }
    }

    public static void main(String[] args){
        int a[] = {8,1};
        int b[] = {0};
        ListNode l1 = null;
        ListNode l2 = null;
        for(int i=0;i< a.length;i++){
            ListNode p = new ListNode(a[i]);
            if(l1 == null){
                l1 = p;
                p.next = null;
            }else{
                p.next = l1;
                l1 = p;
            }
        }

        for(int i=0;i< b.length;i++){
            ListNode p = new ListNode(b[i]);
            if(l2 == null){
                l2 = p;
                p.next = null;
            }else{
                p.next = l2;
                l2 = p;
            }
        }
        print_list(l1);
        System.out.println();
        print_list(l2);
        System.out.println();
        print_list(addTwoNumbers(l1,l2));
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}