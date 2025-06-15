import java.util.*;

class Solution {
    public String reverseWords(String s) {
        // at least one space
        // leading or trailing spaces 
        // concatenated by a single space.
        // stack
        String[] split = s.trim().split("\\s+");
        // System.out.println(Arrays.toString(split));
        StringBuilder result = new StringBuilder();
        for (int i = split.length - 1; i >= 0; i--) {
            result.append(split[i]);
            result.append(" ");
        }
        return result.toString().substring(0, result.length() - 1);
    }
}