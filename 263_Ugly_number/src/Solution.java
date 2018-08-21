class Solution {
    public boolean isUgly(int num) {
        int a[] = {2, 3, 5};
        boolean is_ok = false;
        if (num == 1) {
            return true;
        } else if (num == 0) {
            return false;
        } else {
            for (int item : a) {
                if (num % item == 0) {
                    num = num / item;
                } else {
                    continue;
                }
                is_ok = isUgly(num);
                if (is_ok) {
                    break;
                }
            }
        }
        return is_ok;
    }

    public boolean isUgly2(int num) {
        for (int i = 2; i < 6; i++) {
            while(num % i == 0){
                num = num / i;
            }
        }
        return num == 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isUgly(42));
    }
}