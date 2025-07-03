class Solution {
    public int findCircleNum(int[][] isConnected) {
        int result = 0;
        boolean[] visited = new boolean[isConnected.length];
        //각 도시를 돌며
        for (int i = 0; i <isConnected.length; i++) {
            //아직 방문하지 않았다면 
            if (!visited[i]) {
                //연결된 모든 도시들을 방문처리한다.
                visit(i, isConnected, visited);
                result++;
            }
        }
        return result;
    }

    private void visit(int city, int[][] isConnected, boolean[] visited) {
        //현재 도시를 방문처리하고
        visited[city] = true;

        //현재 도시에서 연결된 도시 중 방문하지 않은 도시들만 방문한다.
        for (int i = 0; i < isConnected[city].length; i++) {
            if (isConnected[city][i] == 1 && !visited[i]) {
                visit(i, isConnected, visited);
            }
        }
    }
}