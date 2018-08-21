class Solution {
    public String reverseString(String s) {
        char[] strs = s.toCharArray();
        int i = 0;
        int j = strs.length - 1;
        while (i < j) {
            char temp = strs[i];
            strs[i] = strs[j];
            strs[j] = temp;
            i++;
            j--;
        }
        return new String(strs);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseString("abc"));
    }
}