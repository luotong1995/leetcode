import org.omg.PortableInterceptor.INACTIVE;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    public static int numsSqures(int n){
        ArrayList<Integer> squres = generateSqures(n);
        Queue<Integer> queue = new LinkedList<>();
        boolean[] marked = new boolean[n + 1];
        int nums = 0;
        queue.add(n);
        // 一层一层遍历
        while(!queue.isEmpty()){
            int size = queue.size();
            nums ++;
            while(size-- > 0){
                int cur = queue.poll();
                for(int item :squres){
                    int next = cur -item;
                    if(next == 0){
                        return nums;
                    }
                    if(next < 0){
                        break;
                    }
                    if(marked[next]){
                        continue;
                    }
                    marked[next] = true;
                    queue.add(next);
                }
            }
        }
        return n;
    }


    public static ArrayList<Integer> generateSqures(int n){
        ArrayList<Integer> list = new ArrayList<>();
        int squre = 1;
        int index = 1;
        while(squre <= n){
            list.add(squre);
            index ++;
            squre = squre + 2*index - 1;
        }
        return list;
    }

    public static void main(String[] args) {
        System.out.println(generateSqures(9));
        System.out.println(numsSqures(11));
    }
}
