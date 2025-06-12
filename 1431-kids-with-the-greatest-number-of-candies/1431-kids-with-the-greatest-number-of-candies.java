class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // find greatest max o n
        // for each kid, if i + extra >= max insert true. o n
        // 2n
        int max = -1;
        for (int candy : candies) {
            if (candy > max) {
                max = candy;
            }
        }

        List<Boolean> result = new ArrayList<>();
        for (int candy : candies) {
            if (candy + extraCandies >= max) {
                result.add(true);
            } else {
                result.add(false);
            }
        }

        return result;
    }
}