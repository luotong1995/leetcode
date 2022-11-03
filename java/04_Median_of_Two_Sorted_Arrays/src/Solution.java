import java.util.ArrayList;

public class Solution {

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int a,b;
        a = b = 0;
        int mid = (nums1.length + nums2.length) / 2;
        if ((nums1.length + nums2.length) %2 == 0){
            a = mid -1;
            b = mid;
        }else{
            a = mid;
        }

        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0, j =0; i < nums1.length || j < nums2.length;){
            if(i < nums1.length && j < nums2.length) {
                if (nums1[i] < nums2[j]) {
                    list.add(nums1[i]);
                    i++;
                } else {
                    list.add(nums2[j]);
                    j++;
                }
            }else if(i < nums1.length && !(j < nums2.length)){
                list.add(nums1[i]);
                i++;
            }else if(!(i < nums1.length) && j < nums2.length){
                list.add(nums2[j]);
                j++;
            }
        }
        if(b !=0 ){
            return (list.get(a) + list.get(b)) / 2.0;
        }else{
            return list.get(a);
        }
    }

    public static void main(String[] args){
        int a[] = {3};
        int b[] = {1,2};
        System.out.println(findMedianSortedArrays(a,b));
    }
}
