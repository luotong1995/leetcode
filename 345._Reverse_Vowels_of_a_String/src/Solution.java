class Solution {
    public static char[] vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'};

    public String reverseVowels(String s) {
        char[] strs = s.toCharArray();
        int i = 0;
        int j = strs.length - 1;
        while (i < j) {
            while (i < strs.length && !isVowels(strs[i])) {
                i++;
            }

            while (j >= 0 && !isVowels(strs[j])) {
                j--;
            }

            if (i < j) {
                char temp = strs[i];
                strs[i] = strs[j];
                strs[j] = temp;
                i++;
                j--;
            }
        }
        return new String(strs);
    }

    public static boolean isVowels(char ch) {
        for (char item : vowels) {
            if (ch == item) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String str = ".,";
        Solution solution = new Solution();
        String re = solution.reverseVowels(str);
        System.out.println(re);
    }
}