import java.util.Scanner;

class Solution {
    // cur = last1 + last2    假设现在为i 现在这一次的解法，可以由第i-1个台阶一下走一个台阶，和第i-2个台阶一下走两个台阶，都是走一步，所以
    //
    public static int climbStairs(int n) {
        if(n <= 2){
            return n;
        }
        int cur = 0;
        int pre1 = 1,pre2 = 2;
        for(int i = 3;i <= n;i++){
            cur = pre1 + pre2;
            pre1 = pre2;
            pre2 = cur;
        }
        return cur;
    }


    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(climbStairs(n));
    }
}