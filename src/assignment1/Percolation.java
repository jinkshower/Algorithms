package assignment1;

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private final int size;
    private final boolean[][] grid;
    private final WeightedQuickUnionUF unionUF;
    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        size = n;
        grid = new boolean[n][n];
        unionUF = new WeightedQuickUnionUF(n * n + 2);
        for (int i = 1; i <= n; i++) {
            unionUF.union(0, i);
            unionUF.union(n * n + 1, n * n + 1 - i);
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (isOpen(row, col)) {
            return;
        }
        grid[row][col] = true;
        if (row == 1) {
            return;
        }
        if (row == size) {
            return;
        }
        if (isOpen(row - 1, col)) {
            unionUF.union(serialized(row - 1, col), serialized(row, col));
        }
        if (col > 1 && isOpen(row, col -1)) {
            unionUF.union(serialized(row, col - 1), serialized(row, col));
        }
        if (col < size && isOpen(row, col + 1)) {
            unionUF.union(serialized(row, col + 1), serialized(row, col));
        }
        if (isOpen(row + 1, col)) {
            unionUF.union(serialized(row + 1, col), serialized(row, col));
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        return grid[row][col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        return unionUF.find(0) == unionUF.find(serialized(row, col));
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        int count = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (grid[i][j]) count++;
            }
        }
        return count;
    }

    // does the system percolate?
    public boolean percolates() {
        return unionUF.find(0) == unionUF.find(size * size + 1);
    }

    private int serialized(int i, int j) {
        return (i - 1) * size + j;
    }
}
