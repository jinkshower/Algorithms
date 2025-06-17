import java.util.*;

class Solution {
    public int maxArea(int[] height) {
        int max = -1;
        int lt = 0;
        int rt = height.length - 1;
        while (lt < rt) {
            int width = rt - lt;
            int minHeight = Math.min(height[lt], height[rt]);
            System.out.println(minHeight);
            max = Math.max(max , width * minHeight);
            if (height[lt] <= height[rt]) {
                lt++;
            } else {
                rt--;
            }
        }
        return max;
    }
}