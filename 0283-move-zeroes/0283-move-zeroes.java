import java.util.*;

class Solution {
    public void moveZeroes(int[] nums) {
        List<Integer> nonZeros = new ArrayList<>();
        int zeroCount = 0;
        for (int num : nums) {
            if (num == 0) {
                zeroCount++;
            } else {
                nonZeros.add(num);
            }
        }

        for (int i = 0; i < nonZeros.size(); i++) {
            nums[i] = nonZeros.get(i);
        }
        for (int i = nonZeros.size(); i < nonZeros.size() + zeroCount; i++) {
            nums[i] = 0;
        }
    }
}