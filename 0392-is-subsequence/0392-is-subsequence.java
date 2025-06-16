class Solution {
    public boolean isSubsequence(String s, String t) {
        int lt = 0;
        if (s.equals(t)) {
            return true;
        }

        for (int rt = 0; rt < t.length(); rt++) {
            if (lt < s.length() && t.charAt(rt) == s.charAt(lt)) {
                lt++;
            }
            if (lt >= s.length()){
                return true;
            }
        }
        return false;
    }
}