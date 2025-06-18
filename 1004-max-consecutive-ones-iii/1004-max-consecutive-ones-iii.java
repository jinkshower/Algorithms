import java.util.*;

class Solution {
    public int longestOnes(int[] nums, int k) {
        int lt = 0;
        int flipCount = k;
        int maxLength = 0;
        for (int rt = 0; rt < nums.length; rt++) {
            if (nums[rt] == 0) {
                flipCount--;
            }

            while (flipCount < 0) {
                if (nums[lt] == 0) {
                    flipCount++;
                }
                lt++;
            }

            maxLength = Math.max(maxLength, rt - lt + 1);
        }

        return maxLength;
    }
}