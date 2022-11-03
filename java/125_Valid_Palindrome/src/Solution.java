class Solution {
    public boolean isPalindrome(String s) {
        String new_str = s.toLowerCase();
        char[] strs = new_str.toCharArray();
        int i = 0;
        int j = strs.length - 1;
        while (i < j) {
            while (i < j && !(strs[i] >= 'a' && strs[i] <= 'z' || strs[i] >= '0' && strs[i] <= '9')) {
                i++;
            }
            while (i < j && !(strs[j] >= 'a' && strs[j] <= 'z' || strs[j] >= '0' && strs[j] <= '9')) {
                j--;
            }
            if(strs[i] != strs[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isPalindrome("A man, a plan, a canal: Panama"));
    }
}