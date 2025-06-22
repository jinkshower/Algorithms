import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int a : arr) {
            int count = map.getOrDefault(a, 0);
            map.put(a, count + 1);
        }
        // if size of keySet and Set of values equal
        Set<Integer> keySet = map.keySet();
        Set<Integer> valueSet = new HashSet<>(map.values());
        return keySet.size() == valueSet.size();
    }
}