class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int length1 = str1.length();
        int length2 = str2.length();

        if (!isDividable(str1, str2)) {
            return "";
        }

        int gcd = gcd(length1, length2);
        return str1.substring(0, gcd);
    }

    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    private boolean isDividable(String first, String second) {
        if ((first + second).equals((second + first))) {
            return true;
        }
        return false;
    }
}