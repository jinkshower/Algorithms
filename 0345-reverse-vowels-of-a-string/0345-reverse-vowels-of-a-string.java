import java.util.*;

class Solution {
    public String reverseVowels(String s) {
        // IceCreAm
        //    ^^
        // search towards middle. if found vowel, stop and swap lt ++ rt -- 
        // until crossed
        // no more vowel -> have to check each iteration if lt and rt crossed
        int lt = 0;
        int rt = s.length() - 1;
        char[] chars = s.toCharArray();

        while (lt < rt) {
            // move lt
            while (!isVowel(chars[lt])) {
                lt++;

                if (lt >= rt) {
                    break;
                }
            }
            // move rt
            while (!isVowel(chars[rt])) {
                rt--;

                if (lt >= rt) {
                    break;
                }
            }
            if (lt >= rt) {
                break;
            }
            // swap
            swap(chars, lt, rt);
            lt++;
            rt--;
        }
        return new String(chars);
    }

    private void swap(char[] chars, int a, int b) {
        char tmp;
        tmp = chars[a];
        chars[a] = chars[b];
        chars[b] = tmp;
    }

    private boolean isVowel(char c) {
        //TODO make a list and use contains.
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            return true;
        }
        return false;
    }
}