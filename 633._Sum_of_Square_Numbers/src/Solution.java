public class Solution {
    public boolean judgeSquareSum(int c) {
        int i = 0;
        int j = (int) Math.sqrt(c);
        while (i <= j) {
            int temp = i * i + j * j;
            if (temp == c) {
                return true;
            } else if (temp > c) {
                j--;
            } else {
                i++;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.judgeSquareSum(4));
    }
}
