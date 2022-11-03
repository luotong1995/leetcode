import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static int[] twoSum(int[] nums, int target) {
        int a[] = {0, 0};
        int i = 0;
        int j = 0;
        for (i = 0; i < nums.length; i++) {
            for (j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    a[0] = i;
                    a[1] = j;
                    break;
                }
            }
        }
        return a;
    }

    // 对于一个有序的序列，可以使用一个左右指针
    public static int[] twoSum5(int[] nums, int target) {
        int i, j;
        i = 0;
        j = nums.length - 1;
        while (i < j) {
            int temp = nums[i] + nums[j];
            if (temp == target) {
                return new int[]{i + 1, j + 1};
            } else if (temp > target) {
                j--;
            } else {
                i++;
            }
        }
        return null;
    }

    // 使用hashMap
    public static int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int temp = target - nums[i];
            if (map.containsKey(temp) && map.get(temp) != i) {
                return new int[]{i, map.get(temp)};
            }
        }
        return new int[]{0, 0};
    }


    public int[] twoSum3(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    public int[] twoSum4(int[] nums, int target) {
        int[] indices = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            indices[i] = i;
        }
        sort(nums, indices);
        int l = 0;
        int r = nums.length - 1;
        int sum = 0;
        while (l < r) {
            sum = nums[l] + nums[r];
            if (sum > target) {
                r--;
            } else if (sum < target) {
                l++;
            } else {
                return new int[]{indices[l], indices[r]};
            }
        }
        return new int[]{-1, -1};
    }

    public static void sort(int[] nums, int[] indices) {
        for (int i = 0; i < nums.length; i++) {
            heapInsert(nums, indices, i);
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            swap(nums, indices, 0, i);
            heapify(nums, indices, i);
        }
    }


    public static void heapify(int[] nums, int[] indices, int length) {
        //交换往堆顶元素和堆底元素后，重新调整堆，此时不对第i个节点进行调整，因为此时的length为整个堆中最大堆元素的
        //对堆的前面的节点进行重新调整堆。
        //从堆顶开始逐渐开始调整
        int left = 1;
        int right = 2;
        int large;
        int i = 0;
        while (left < length) {
            large = nums[left] > nums[i] ? left : i;

            large = right < length && nums[right] > nums[large] ? right : large;
            if (large == i) {
                break;
            }
            swap(nums, indices, large, i);
            i = large;
            left = 2 * i + 1;
            right = 2 * i + 2;
        }

    }

    public static void heapInsert(int[] nums, int[] indices, int i) {
        while (i > 0) {
            int p = (i - 1) / 2;
            if (nums[i] <= nums[p]) {
                break;
            }
            swap(nums, indices, i, p);
            i = p;
        }
    }


    public static void swap(int[] nums, int[] indices, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
        temp = indices[a];
        indices[a] = indices[b];
        indices[b] = temp;
    }


}

