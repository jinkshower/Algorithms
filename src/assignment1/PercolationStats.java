package assignment1;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private int num_of_ex;
    private double[] outcomes;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        num_of_ex = trials;
        outcomes = new double[trials];
        for (int i = 0; i < trials; i++) {
            Percolation grid = new Percolation(n);
            while (!grid.percolates()){
                int x = StdRandom.uniformInt(n) +1;
                int y = StdRandom.uniformInt(n) +1;
                if (!grid.isOpen(x, y)) {
                    grid.open(x, y);
                    outcomes[i]++;
                }
            }
            outcomes[i] /= n*n;
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(outcomes);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(outcomes);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return this.mean() - 1.96 * this.stddev() / Math.sqrt(num_of_ex);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return this.mean() + 1.96 * this.stddev() / Math.sqrt(num_of_ex);
    }
    public static void main(String[] args) {
        System.out.println("Input size of grid: ");
        int N = StdIn.readInt();
        System.out.println("Input number of experiments");
        int T = StdIn.readInt();
        PercolationStats percstats = new PercolationStats(N, T);
        System.out.println("mean = " + percstats.mean());
        System.out.println("stddev = " + percstats.stddev());
        System.out.println("95% confidence interval = [" + percstats.confidenceLo() + ", " + percstats.confidenceHi());
    }
}
