import javafx.util.Pair;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    public static int minPathLength(int[][] grids, int tr, int tc) {
        // 表示点走的方向，{1，0}表示向下走一格，{-1，0}表示向上走一格, {0,1}表示向右走一格，{0,-1}表示向左走一格
        final int[][] direction = {{1, 0},
                        {-1, 0},
                        {0, 1},
                        {0, -1}};
        final int m = grids.length, n = grids[0].length;

        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.add(new Pair<>(0, 0));
        int pathLength = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            pathLength++;
            while (size-- > 0) {
                Pair<Integer, Integer> cur = queue.poll();
                // 四个方向都尝试一下
                for (int[] d : direction) {
                    int nr = cur.getKey() + d[0], nc = cur.getValue() + d[1];
                    Pair<Integer, Integer> next = new Pair<>(nr, nc);
                    if (next.getKey() < 0 || next.getKey() >= m
                            || next.getValue() < 0 || next.getValue() >= n || grids[next.getKey()][next.getValue()] == 0) {

                        continue;
                    }
                    grids[next.getKey()][next.getValue()] = 0; // 标记
                    if (next.getKey() == tr && next.getValue() == tc) {
                        return pathLength;
                    }
                    queue.add(next);
                }
            }
        }
        return -1;
    }


    public static void main(String[] args) {
        int[][] grids = {{1, 1, 0, 1},
                        {1, 0, 1, 0},
                        {1, 1, 1, 1},
                        {1, 0, 1, 1}};
        System.out.println(minPathLength(grids, 3,3));

    }


}
