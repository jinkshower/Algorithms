class Solution {
    public int largestAltitude(int[] gain) {
        int[] result = new int[gain.length + 1];
        int max = 0;
        for (int i = 0; i < gain.length; i++) {
            result[i + 1] = result[i] + gain[i];
            max = Math.max(max, result[i + 1]);
        }
        return max;
    }
}