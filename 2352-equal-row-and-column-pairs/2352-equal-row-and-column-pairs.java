import java.util.*;

class Solution {
    public int equalPairs(int[][] grid) {
        List<List<Integer>> rows = new ArrayList<>();
        List<List<Integer>> columns = new ArrayList<>();

        for (int i = 0; i < grid.length; i++) {
            List<Integer> row = Arrays.stream(grid[i]).boxed().toList();
            rows.add(row);
        }
        for (int i = 0; i < grid.length; i++) {
            List<Integer> column = new ArrayList<>();
            for (int j = 0; j < grid.length; j++) {
                column.add(grid[j][i]);
            }
            columns.add(column);
        }
        int count = 0;
        for (List<Integer> row : rows) {
            for (List<Integer> column : columns) {
                if (row.equals(column)) {
                    count++;
                }
            }
        }

        return count;
    }
}