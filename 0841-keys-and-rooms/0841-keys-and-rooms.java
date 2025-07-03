import java.util.*;

class Solution {
    
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        dfs(visited, 0, rooms);

        for (boolean v : visited) {
            if (!v) {
                return false;
            }
        }
        return true;
    }

    private void dfs(boolean[] visited, int room, List<List<Integer>> rooms) {
        visited[room] = true;

        for (int key : rooms.get(room)) {
            if (!visited[key]) {
                dfs(visited, key, rooms);
            }
        }
    }
}