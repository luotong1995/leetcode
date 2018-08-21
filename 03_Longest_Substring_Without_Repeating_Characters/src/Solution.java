
import java.util.*;

public class Solution {

    public static int lengthOfLongestSubstring(String s) {
        int i, j;
        i = 0;
        int final_length = 0;
        for (i = 0; i < s.length(); i++) {
            ArrayList<String> list = new ArrayList<>();
            int length = 1;
            char c = s.charAt(i);
            list.add(String.valueOf(c));
            if (final_length < length) {
                final_length = length;
            }
            for (j = i + 1; j < s.length(); j++) {
                char temp = s.charAt(j);
                if (list.contains(String.valueOf(temp))) {
                    if (final_length < length) {
                        final_length = length;
                    }
                    break;
                }else {
                    list.add(String.valueOf(temp));
                    length++;
                }
            }
            if(j == s.length()){
                if (final_length < length) {
                    final_length = length;
                }
            }
        }
        return final_length;
    }

    public static String lengthOfLongestSubstring2(String s) {
        Map<Integer,String> map = new HashMap<>();
        int i,j;
        i = 0;
        int final_length = 0;
        for(i = 0; i<s.length(); i++){
            ArrayList<String> list = new ArrayList<>();
            int length = 1;
            char c = s.charAt(i);
            list.add(String.valueOf(c));
            if(final_length < length){
                final_length = length;
                StringBuilder sb = new StringBuilder();
                for (String item:list){
                    sb.append(item);
                }
                map.put(final_length,sb.toString());
            }
            for(j = i + 1; j < s.length(); j++){
                char temp = s.charAt(j);
                if (list.contains(String.valueOf(temp))){
                    if(final_length < length){
                        final_length = length;
                        StringBuilder sb = new StringBuilder();
                        for (String item:list){
                            sb.append(item);
                        }
                        map.put(final_length,sb.toString());
                    }
                    break;
                }
                else{
                    list.add(String.valueOf(temp));
                    length ++;
                }
            }
            if(j == s.length()){
                if (final_length < length) {
                    final_length = length;
                    StringBuilder sb = new StringBuilder();
                    for (String item:list){
                        sb.append(item);
                    }
                    map.put(final_length,sb.toString());
                }
            }

        }
        return map.get(final_length);
    }


    // 滑动窗口，实现最短子序列
    public int lengthOfLongestSubstring3(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }

    public static void main(String [] args){

        int a  = lengthOfLongestSubstring("jbpnbwwd");
        System.out.print(a);
    }

}
