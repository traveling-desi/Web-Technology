

public class Percolation_bottom_open_sites_array {

	private WeightedQuickUnionUF mPerc1;
	private int mGridsize;
	private int mTopVertex;
	private boolean[] mGridOpen;
	private int mBottomVertex;
	private int[] mBottomisOpen;
	private int mBottomisOpen_ptr;
	private boolean mPercolates;

	// create N-by-N grid, with all sites blocked
	// value of 0 in array means site blocked.
	public Percolation_bottom_open_sites_array(int N) {

		if (N < 1) {
			throw new IllegalArgumentException("Bad N value");
		}

		int size = N * N + 2;

		// Array if a site is open or not.
		// Array initialized by default with 0 (site blocked)
		// if site is 1 then site is open.
		// TopVertex and BottomVertex initialized as open.
		mGridOpen = new boolean[size];
		mTopVertex = 0;
		mBottomVertex = size -1;
		mGridOpen[mTopVertex] = true;
		mGridOpen[mBottomVertex] = true;
		mGridsize = N;
		
	
		mPerc1 = new WeightedQuickUnionUF(size);
		
		mBottomisOpen= new int[N];
		
//		for (int i = 0; i < mBottomisOpen.length; i++)
//			System.out.println(mBottomisOpen[i]);
		mBottomisOpen_ptr = 0;
		
		mPercolates = false;
		
	}

	// open site (row i, column j) if it is not already
	public void open(int i, int j) {

		if (checkIndex(i, j)) {
			int arrIndex = findArrIndex(i, j);
			
			if (i == mGridsize && !mGridOpen[arrIndex]) {
				mBottomisOpen[mBottomisOpen_ptr++] = arrIndex;
			}
			
			
			mGridOpen[arrIndex] = true;
					
			if (i != 1) {
				if (mGridOpen[arrIndex - mGridsize]) {
					mPerc1.union(arrIndex, arrIndex - mGridsize);
				}
				
			} else {
				mPerc1.union(arrIndex, mTopVertex);
				//System.out.println("I was here");
			}
			
			if (i != mGridsize) {
				if (mGridOpen[arrIndex + mGridsize]) {
					mPerc1.union(arrIndex, arrIndex + mGridsize);
				}
			} 
			
			if (j != mGridsize && mGridOpen[arrIndex + 1]) {	
				mPerc1.union(arrIndex, arrIndex + 1);
			}
					
			
			if (j != 1 && mGridOpen[arrIndex - 1]) {
				mPerc1.union(arrIndex, arrIndex - 1);
			}
			
			if (!mPercolates) {
				int comp1 = mPerc1.find(mTopVertex);
				for (int k = 0; k < mBottomisOpen_ptr; k++) {
					if (comp1 == mPerc1.find(mBottomisOpen[k])) {
						mPerc1.union(mBottomVertex,mBottomisOpen[k]);
						mPercolates = true;
						break;
					}
				}
			}
		
		}
	}

	// is site (row i, column j) open?
	public boolean isOpen(int i, int j) {
		if (checkIndex(i, j)) {
			int arrIndex = findArrIndex(i, j);
			return (mGridOpen[arrIndex]);
		} else {
			return false;
		}
	}

	// is site (row i, column j) full?
	public boolean isFull(int i, int j) {
		if (checkIndex(i, j)) {
			int arrIndex = findArrIndex(i, j);
			return (mPerc1.connected(arrIndex, mTopVertex));
		} else {
			return false;
		}
	}

	// does the system percolate?
	public boolean percolates() {
		return (mPerc1.connected(mBottomVertex, mTopVertex));

	}

	// Checks if the correct index is passed into the program
	private boolean checkIndex(int i, int j) {
		// TODO Auto-generated method stub
		if (i < 1 || i > mGridsize || j < 1 || j > mGridsize) {
			throw new IndexOutOfBoundsException(
					"i and j values need to be between 1 and " + mGridsize);
		}
		return true;
	}

	// Changes from 2-D array coordinates to 1-D list index
	private int findArrIndex(int i, int j) {
		int arrIndex = ((i - 1) * mGridsize + j);
		return arrIndex;
	}
};
