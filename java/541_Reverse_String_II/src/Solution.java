class Solution {
    public String reverseStr(String s, int k) {
        // 每隔K个元素就需要reverse一下
        char[] strs = s.toCharArray();
        int start = 0;
        int end = (k - 1) <= (strs.length - 1) ? k - 1 : strs.length - 1;
        while (start < end && start < strs.length && end <= strs.length) {
            reverseString(strs, start, end);
            start = (start + 2 * k) < strs.length - 1 ? (start + 2 * k) : strs.length - 1;
            end = (start + k - 1) <= strs.length - 1 ? (start + k - 1) : strs.length - 1;
        }
        return new String(strs);
    }


    public void reverseString(char[] strs, int start, int end) {
        int i = start;
        int j = end;
        while (i < j) {
            char temp = strs[i];
            strs[i] = strs[j];
            strs[j] = temp;
            i++;
            j--;
        }
    }

    // 同样的思路别人写的代码很简单
    public String reverseStr2(String s, int k) {
        char[] ca = s.toCharArray();
        for (int left = 0; left < ca.length; left += 2 * k) {
            for (int i = left, j = Math.min(left + k - 1, ca.length - 1); i < j; i++, j--) {
                char tmp = ca[i];
                ca[i] = ca[j];
                ca[j] = tmp;
            }
        }
        return new String(ca);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseStr("abcdefg", 2));
    }
}