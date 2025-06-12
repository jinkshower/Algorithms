class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        int[] copy = new int[flowerbed.length + 2];

        for (int i = 1; i <= flowerbed.length; i++) {
            copy[i] = flowerbed[i - 1];
        }

        for (int i = 1; i <= flowerbed.length; i++) {
            if (canplace(copy, i)) {
                copy[i] = 1;
                n--;
            }
        }

        return n <= 0 ? true : false;
    }

    private boolean canplace(int[] flowerbed, int idx) {
        if (flowerbed[idx - 1] == 0 && flowerbed[idx + 1] == 0 && flowerbed[idx] == 0) {
            return true;
        }
        return false;
    }
}