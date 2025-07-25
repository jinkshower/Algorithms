import java.util.*;

class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()){
            if (c == '*') {
                stack.pop();
                continue;
            }
            stack.push(c);
        }
        System.out.println(stack);
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        return sb.toString();
    }
}