import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // O(n) without division operation
        // 5 <- 1 
        // bcd acd abd abc
        //1 [1, 2, 6, 24] 1 
        //  a  ab abc abcd
        //1 [24, 24, 12, 4] 1
        //  dcba dcb dc d
        
        // initialize
        // 4
        int len = nums.length;
        int[] prefix = new int[len + 2];
        int[] suffix = new int[len + 2];
        prefix[0] = 1;
        suffix[0] = 1;
        prefix[len + 1] = 1;
        suffix[len + 1] = 1;

        for (int i = 0; i < len; i++) {
            prefix[i + 1] = nums[i] * prefix[i];
        }

        for (int i = len - 1; i >= 0; i--) {
            suffix[i + 1] = nums[i] * suffix[i + 2];
        }

        // System.out.println(Arrays.toString(prefix));
        // System.out.println(Arrays.toString(suffix));

        //[1, 1, 2, 6, 24, 1] prefix
        // [1, 24, 24, 12, 4, 1] suffix

        int[] result = new int[len];
        for (int i = 0; i < len; i++) {
            result[i] = prefix[i] * suffix[i + 2];
        }
        
        return result;
    }
}