class Solution {
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r))
                return isPalindromic(s, l + 1, r) || isPalindromic(s, l, r - 1);
            l++;
            r--;
        }
        return true;
    }


    public boolean isPalindromic(String s, int l, int r) {
        while (l < r)
            if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }

    public boolean validPalindrome2(String s) {
        // 每个元素一个一个的删除
        char[] strs = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            char[] strs2 = delIindex(strs, i);
            if (isPalindromic(new String(strs2))) {
                return true;
            }
        }
        return false;
    }

    public char[] delIindex(char[] strs, int index) {
        char[] new_chars = new char[strs.length - 1];
        int t = 0;
        for (int i = 0; i < strs.length; i++) {
            if (i != index) {
                new_chars[t++] = strs[i];
            }
        }
        return new_chars;
    }

    public boolean isPalindromic(String s) {
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r))
                return false;
            l++;
            r--;
        }
        return true;
    }


    // 此问题是可以使用前后两个指针来进行，
    // 如果遇到不相等的，
    // 1.尝试的前面后移一个再判断，如果不行再尝试后面前移一位
    // 2.尝试的后面前移一个再判断，如果不行再尝试前面后移一位
    public boolean validPalindrome3(String s) {
        int i = 0;
        int j = s.length() - 1;
        char[] strs = s.toCharArray();
        int count = 0;
        boolean valid1 = true;
        while (i < j) {
            if (strs[i] == strs[j]) {
                i++;
                j--;
            } else {
                if (strs[i + 1] == strs[j]) {
                    i++;
                    count++;
                    continue;
                } else if (strs[i] == strs[j - 1]) {
                    j--;
                    count++;
                    continue;
                } else {
                    valid1 = false;
                    break;
                }
            }
        }
        valid1 = valid1 && count <= 1;
        i = 0;
        j = s.length() - 1;
        count = 0;
        boolean valid2 = true;
        while (i < j) {
            if (strs[i] == strs[j]) {
                i++;
                j--;
            } else {
                if (strs[i] == strs[j - 1]) {
                    j--;
                    count++;
                    continue;
                } else if (strs[i + 1] == strs[j]) {
                    i++;
                    count++;
                    continue;
                } else {
                    valid2 = false;
                    break;
                }
            }
        }
        valid2 = valid2 && count <= 1;
        boolean valid = valid1 || valid2;
        return valid;
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.validPalindrome("eeccccbebaeeabebccceea"));
    }
}