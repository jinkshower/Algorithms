class Solution {
    public int pivotIndex(int[] nums) {
        int[] prefix = new int[nums.length + 2];
        int[] suffix = new int[nums.length + 2];

        for (int i = 0; i < nums.length; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            suffix[i + 1] = suffix[i + 2] + nums[i];
        }

        for (int i = 1; i <= nums.length; i++) {
            if (prefix[i - 1] == suffix[i + 1]) {
                return i - 1;
            }
        }
        return -1;
    }
}