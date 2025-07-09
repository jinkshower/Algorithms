import java.util.*;

class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        List<int[]> pairs = new ArrayList<>();
        for (int i = 0; i < nums1.length; i++) {
            pairs.add(new int[]{nums1[i], nums2[i]});
        }

        pairs.sort((a, b) -> b[1] - a[1]);

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        long sum = 0;
        long result = -1;

        for (int[] pair : pairs) {
            sum += pair[0];
            
            minHeap.offer(pair[0]);  
            if (minHeap.size() > k) {
                int popped = minHeap.poll();
                sum -= popped; 
            }
            if (minHeap.size() == k) {
                result = Math.max(result, sum * pair[1]);
            }
        }
        return result; 
    }
}