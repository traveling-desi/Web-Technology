import java.util.Arrays;

public class Board {

	private int[][] gmBoard;
	private int gmSize;
	private int blankrow;
	private int blankcol;

	// construct a board from an N-by-N array of blocks
	// (where blocks[i][j] = block in row i, column j)
	public Board(int[][] blocks) {
		if (blocks != null) {
			this.gmSize = blocks[0].length;
			gmBoard = new int[this.gmSize][this.gmSize];

			for (int i = 0; i < this.gmSize; i++) {
				for (int j = 0; j < this.gmSize; j++) {
					if (blocks[i][j] == 0) {
						blankrow = i;
						blankcol = j;
					}
					gmBoard[i][j] = blocks[i][j];
				}
			}
		} else {
			throw new IllegalArgumentException();
		}
	}

	// board dimension N
	public int dimension() {
		return this.gmSize;

	}

	// number of blocks out of place
	public int hamming() {
		int hamming = 0;
		for (int i = 0; i < this.gmSize; i++) {
			for (int j = 0; j < this.gmSize; j++) {
				if (this.gmBoard[i][j] != 0
						&& this.gmBoard[i][j] != ((i * this.gmSize) + j + 1)) {
					hamming++;
				}
			}
		}
		return hamming;
	}

	// sum of Manhattan distances between blocks and goal
	public int manhattan() {
		int manhattan = 0;
		for (int i = 0; i < this.gmSize; i++) {
			for (int j = 0; j < this.gmSize; j++) {
				if (this.gmBoard[i][j] != 0) {
					int real_i = ((this.gmBoard[i][j] - 1) / this.gmSize);
					int real_j = ((this.gmBoard[i][j] - 1) % this.gmSize);
					manhattan += java.lang.Math.abs(i - real_i);
					manhattan += java.lang.Math.abs(j - real_j);
				}
			}
		}
		return manhattan;
	}

	// is this board the goal board?
	public boolean isGoal() {
		for (int i = 0; i < this.gmSize; i++) {
			for (int j = 0; j < this.gmSize; j++) {
				if (i == (this.gmSize-1) && j == (this.gmSize-1)) {
					if (this.gmBoard[i][j] != 0)
						return false;
				} else {
					if (this.gmBoard[i][j] != ((i * this.gmSize) + j + 1)) 
						return false;
				}
			}
		}
//		System.out.println("HERE");
		return true;
	}

	// a board obtained by exchanging two adjacent blocks in the same row
	public Board twin() {
		int randrow;
		int randcol;
		int[][] twinBoard = new int[this.gmSize][this.gmSize];

		for(int i = 0; i < gmSize; i++)
		    twinBoard[i] = gmBoard[i].clone();


		randrow = StdRandom.uniform(0, this.gmSize);
		randcol = StdRandom.uniform(0, this.gmSize - 1);
		if (randrow == blankrow) {
			if (randrow > 0)
				randrow--;
			else
				randrow++;
		} 
		
		twinBoard[randrow][randcol] = gmBoard[randrow][randcol + 1];
		twinBoard[randrow][randcol + 1] = gmBoard[randrow][randcol];
		
		return new Board(twinBoard);
	}

	// does this board equal y?
	public boolean equals(Object y) {
		if (y == null || (y.getClass() != this.getClass())) {
			return false;
		}
		Board that = ((Board) y);
		if ((that.dimension() != this.gmSize)
				|| that.hamming() != this.hamming()
				|| that.manhattan() != this.manhattan()) {
			return false;
		} else {
			if (Arrays.deepEquals(that.gmBoard, this.gmBoard)) {
				return true;
			}
		}
		return false;
	}

	// all neighboring boards
	public Iterable<Board> neighbors() {
		Stack<Board> stboard = new Stack<Board>();

		int[][] nghBoard = new int[this.gmSize][this.gmSize];

		for (int i = 0; i < gmSize; i++)
			nghBoard[i] = gmBoard[i].clone();

		
		if ( blankrow == 0 || blankrow == (gmSize -1) || blankcol == 0 || blankcol == (gmSize -1) ) {
			if ( blankrow == 0 || blankrow == (gmSize -1)) {
				if ( blankrow == 0 ) {
					if ( blankcol == 0 ) { // left top corner
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol+1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow+1, blankcol ));
					} else if ( blankcol == (gmSize -1) ) { // right top corner
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol-1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow+1, blankcol ));
					} else {
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol+1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol-1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow+1, blankcol ));
					}
				} else {   // blankrow == gmSize
					if ( blankcol == 0 ) { // left bottom corner
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol+1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow-1, blankcol ));
					} else if ( blankcol == (gmSize -1)) { // right bottom corner
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol-1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow-1, blankcol ));
					} else {
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol+1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol-1 ));
						stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow-1, blankcol ));
					}
				}
				
			} else {  // blankcol == 0 || blankcol == gmSize
				
				// Note all the corners already take care of in the row statements
				if ( blankcol == 0 ) {
					stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow+1, blankcol ));
					stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow-1, blankcol ));
					stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol+1 ));
				} else {
					stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol-1 ));
					stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow+1, blankcol ));
					stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow-1, blankcol ));
				}
			}
		} else {
			stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol+1 ));
			stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow, blankcol-1 ));
			stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow+1, blankcol ));
			stboard.push(exchtiles(nghBoard, blankrow, blankcol, blankrow-1, blankcol ));
		}
		return stboard;
	}

	
	
	// Exchanges tiles between (x1,y1) and (x2,y2) creates a new board and returns it.
	private Board exchtiles(int[][] nghBoard, int x1, int y1, int x2, int y2) {
		int exchtile1, exchtile2;
		
		// Exchange tiles
		exchtile1 = nghBoard[x1][y1];
		exchtile2 = nghBoard[x2][y2];
		nghBoard[x1][y1] = exchtile2;
		nghBoard[x2][y2] = exchtile1;
		
		// create neighbor
		Board brd = new Board(nghBoard);
		
		// put back tiles in original position
		nghBoard[x1][y1] = exchtile1;
		nghBoard[x2][y2] = exchtile2;
		
		return brd;
		
	}

	// string representation of the board (in the output format specified below)
	public String toString() {
		StringBuilder s = new StringBuilder();
		s.append(this.gmSize + "\n");
		for (int i = 0; i < this.gmSize; i++) {
			for (int j = 0; j < this.gmSize; j++) {
				s.append(String.format("%2d ", this.gmBoard[i][j]));
			}
			s.append("\n");
		}
		return s.toString();
	}
}
