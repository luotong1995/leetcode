class Solution {
    public String reverseWords(String s) {
        char[] strs = s.toCharArray();
        for (int i = 0; i < strs.length; ) {
            int j = i;
            //find space
            while (j < strs.length && strs[j] != ' ') {
                j++;
            }
            reverseString(strs, i, j - 1);
            // 找出在一个开始的指针
            i = j + 1;
        }
        return new String(strs);
    }

    public void reverseString(char[] strs, int i, int j) {
        while (i < j) {
            char temp = strs[i];
            strs[i] = strs[j];
            strs[j] = temp;
            i++;
            j--;
        }
    }

    public String reverseWords2(String s) {
        StringBuilder result = new StringBuilder();
        String[] strings = s.split(" ");
        for (String item : strings) {
            StringBuilder temp = new StringBuilder(item);
            temp.reverse();
            result.append(temp);
            result.append(" ");
        }
        String result1 = result.toString();
        return result1.substring(0,result1.length());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseWords2("Let's take LeetCode contest"));
    }
}