import java.util.*;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // find first k elements' average
        // slide and refresh max 
        double max = 0d;
        double sum = 0d;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        max = sum / k;
        
        for (int i = k; i < nums.length; i++) {
            sum += nums[i];
            sum -= nums[i - k];
            max = Math.max((sum / k), max);
        }

        return max;
    }
}