public class Solution {
    public int getSum(int a, int b) {
        // 不考虑进位可以使用异或运算进行实现
        int sum = a ^ b;
        // 进位可以用与运算进行实现
        int carray = (a & b) << 1;
        while (carray != 0) {
            int i = sum;
            int j = carray;
            sum = i ^ j;
            carray = (i & j) << 1;
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.getSum(2, 3));

    }
}
