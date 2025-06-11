class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder answer = new StringBuilder();
        // word1 first alternatively append char
        int limit1 = word1.length() - 1;
        int limit2 = word2.length() - 1;

        int lt = 0;
        int rt = 0;

        while (lt <= limit1 && rt <= limit2) {
            answer.append(word1.charAt(lt));
            lt++;
            answer.append(word2.charAt(rt));
            rt++;
        }

        // deal with the remainder
        while (lt <= limit1) {
            answer.append(word1.charAt(lt));
            lt++;
        }

        while (rt <= limit2) {
            answer.append(word2.charAt(rt));
            rt++;
        }

        return answer.toString();     
    }
}