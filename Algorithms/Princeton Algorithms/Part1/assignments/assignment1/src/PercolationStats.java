
public class PercolationStats {

	private double[] prob;
	private Percolation perc;

	// perform T independent computational experiments on an N-by-N grid
	public PercolationStats(int N, int T) {

		if (N < 1 || T < 1) {
			throw new IllegalArgumentException("Bad N value");
		}
		
		double mGridSize = N * N;
		prob = new double[T];

		for (int trials = 0; trials < T; trials++) {
			perc = new Percolation(N);
			int opened = 0;
			while(true) {
				int row = StdRandom.uniform(1, N+1);
				int col = StdRandom.uniform(1, N+1);

				if(! perc.isOpen(row, col)) {
					perc.open(row, col);
					opened++;
				}
				if (perc.percolates()) {
					prob[trials] = opened/mGridSize;
					perc = null;
					break;
				}
			}
			
		}
	}

	// sample mean of percolation threshold
	public double mean() {
		
		return StdStats.mean(prob);
	}

	// sample standard deviation of percolation threshold
	public double stddev() {
		
		return StdStats.stddev(prob);
	}

	// returns lower bound of the 95% confidence interval
	public double confidenceLo() {

		double mean = mean();
		double stddev = stddev();
		double root_trials = Math.pow(prob.length,0.5);
		return (mean - ((1.96*stddev)/root_trials));
	}

	// returns upper bound of the 95% confidence interval
	public double confidenceHi() {
		double mean = mean();
		double stddev = stddev();
		double root_trials = Math.pow(prob.length,0.5);
		return (mean + ((1.96*stddev)/root_trials));
	}


	// test client, described below
	public static void main(String[] args) {

		int N = Integer.parseInt(args[0]);
		int T = Integer.parseInt(args[1]);

		PercolationStats percStats = new PercolationStats(N, T);
		System.out.println("mean                    = "+ percStats.mean());
		System.out.println("stddev                  = "+ percStats.stddev());
		System.out.println("95% confidence interval = "+ percStats.confidenceLo() + ", " + percStats.confidenceHi());


	}

}
