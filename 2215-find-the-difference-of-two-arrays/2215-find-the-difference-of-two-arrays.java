class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> result = new ArrayList<>();
        Set<Integer> one = new HashSet<>();
        for (int n : nums1) {
            one.add(n);
        }
        Set<Integer> two = new HashSet<>();
        for (int n : nums2) {
            two.add(n);
        }

        List<Integer> result1 = new ArrayList<>();
        for (int n : one) {
            if (!two.contains(n)) {
                result1.add(n);
            }
        }
        List<Integer> result2 = new ArrayList<>();
        for (int n : two) {
            if (!one.contains(n)){
                result2.add(n);
            }
        }
        
        result.add(result1);
        result.add(result2);
        return result;
    }
}