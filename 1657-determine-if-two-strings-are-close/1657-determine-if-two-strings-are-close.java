import java.util.*;

class Solution {
    public boolean closeStrings(String word1, String word2) {
        // if different size no
        // if contains distinct char no
        // if occurence different no
        if (word1.length() != word2.length()) {
            return false;
        }
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        countOccurence(map1, word1);
        countOccurence(map2, word2);
        if (map1.size() != map2.size()) {
            return false;
        }
        if (!map1.keySet().equals(map2.keySet())) {
            return false;
        }
        List<Integer> one = new ArrayList<>(map1.values());
        List<Integer> two = new ArrayList<>(map2.values());
        one.sort(Comparator.naturalOrder());
        two.sort(Comparator.naturalOrder());

        if (!one.equals(two)){
            return false;
        }

        return true;
    }

    private void countOccurence(Map<Character, Integer> map, String s) {
        for (char c : s.toCharArray()) {
            int count = map.getOrDefault(c, 0);
            map.put(c, count + 1);
        }
    }
}