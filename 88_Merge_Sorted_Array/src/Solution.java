public class Solution {
    // 将两个有序的数组归并到第一个数组中
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index1 = m - 1;
        int index2 = n - 1;
        int merge_idx = m + n - 1;
        while (index1 >= 0 || index2 >= 0) {
            if (index1 < 0) {
                nums1[merge_idx--] = nums2[index2--];
            } else if (index2 < 0) {
                nums1[merge_idx--] = nums1[index1--];
            } else if (nums1[index1] >= nums2[index2]) {
                nums1[merge_idx--] = nums1[index1--];
            } else {
                nums1[merge_idx--] = nums2[index2--];
            }
        }
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int[] nums2 = {2, 5, 6};
        Solution solution = new Solution();
        solution.merge(nums1, 3, nums2, 3);
        for (int item : nums1) {
            System.out.println(item);
        }

    }
}
