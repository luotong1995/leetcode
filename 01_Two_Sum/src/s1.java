import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;

public class s1 {
    public static void main(String[] args) {
//        输入：nums = [2,7,11,15], target = 9
//        输出：[0,1]
//        解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
        int a[] = {3, 2, 4};
        System.out.println(twoSum2(a, 6)[0]);
        System.out.println(twoSum2(a, 6)[1]);
    }


    public static int[] twoSum(int[] nums, int target) {
        int a[] = {0, 0};
        for (int k = 0; k < nums.length; k++) {
            for (int l = k + 1; l < nums.length; l++) {
                if (nums[k] + nums[l] == target) {
                    a[0] = k;
                    a[1] = l;
                }
            }
        }
        return a;
    }

    public static int[] twoSum2(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i]) && map.get(target - nums[i]) != i) {
                return new int[]{i, map.get(target - nums[i])};
            }
        }
        return new int[]{0, 0};
    }
}
