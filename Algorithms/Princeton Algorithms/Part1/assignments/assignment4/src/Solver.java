
public class Solver {

	private MinPQ<SearchNode> minpq = new MinPQ<SearchNode>();
	private MinPQ<SearchNode> twinminpq = new MinPQ<SearchNode>();
	private boolean solved = false;
	private SearchNode glSrchNode;
	


	// find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
    	
    	int moves;
    	
    	SearchNode initSearchNode = new SearchNode(initial, 0, null);
    	minpq.insert(initSearchNode);
    	
    	SearchNode twininitSearchNode = new SearchNode(initial.twin(), 0, null);
    	twinminpq.insert(twininitSearchNode);

    	
    	SearchNode minSrchNode = initSearchNode;
    	SearchNode twinminSrchNode = twininitSearchNode;

    	while ( minSrchNode.brd.isGoal() != true  && twinminSrchNode.brd.isGoal() != true) {

    		minSrchNode = minpq.delMin();
    		twinminSrchNode = twinminpq.delMin();
    		
    		
    		for (Board nghbrs : minSrchNode.brd.neighbors() ){

				if ( minSrchNode.parent != null ) {

					if ( !(minSrchNode.parent).brd.equals(nghbrs) ) {
						moves = minSrchNode.moves + 1;
						minpq.insert(new SearchNode(nghbrs, moves,
								minSrchNode));
					} 
				} else {
					moves = minSrchNode.moves + 1;			
					minpq.insert( new SearchNode(nghbrs, moves,
							minSrchNode ) );
				}
			}

    		
    		for (Board nghbrs : twinminSrchNode.brd.neighbors() ){
				if ( twinminSrchNode.parent != null ) {
					if ( !(twinminSrchNode.parent).brd.equals(nghbrs) ) {
						moves = twinminSrchNode.moves + 1;
						twinminpq.insert(new SearchNode(nghbrs, moves,
								twinminSrchNode));
					}
				} else {	
					moves = twinminSrchNode.moves + 1;		
					twinminpq.insert( new SearchNode(nghbrs, moves,
							twinminSrchNode ) );
				}
			}
    	}
    	
    	if ( minSrchNode.brd.isGoal() == true ) {
    		solved = true;
    	} 
    	glSrchNode = minSrchNode;
    }
    
 // is the initial board solvable?
    public boolean isSolvable()  {
    	return this.solved;
    }
    
   // min number of moves to solve initial board; -1 if no solution
    public int moves()  {
    	if (solved)
    		return glSrchNode.moves;
    	else
    		return -1;
    	
    }
 // sequence of boards in a shortest solution; null if no solution
    public Iterable<Board> solution()    {
    	Stack<Board> stboard = new Stack<Board>();
    	SearchNode lclSrchNode;
    	if (solved) {
    		lclSrchNode = glSrchNode;
    		stboard.push(lclSrchNode.brd);	
    		while ( lclSrchNode.parent != null ) {
    			
    			lclSrchNode = lclSrchNode.parent;
    			stboard.push(lclSrchNode.brd);
    		}
    		return stboard;
    	} else
    		return null;
    }
    
 // solve a slider puzzle (given below)
    public static void main(String[] args)  {
 
    	
    }
    
    
    // Class to define the searchNode
	private class SearchNode implements Comparable<SearchNode> {
		private Board brd;
		private int moves;
		private SearchNode parent;
		
		public SearchNode(Board brd, int moves, SearchNode parent) {
			// TODO Auto-generated constructor stub
			this.brd = brd;
			this.moves = moves;
			this.parent = parent;
		}

		@Override
		public int compareTo(SearchNode that) {
			// TODO Auto-generated method stub
			
			if ( (this.brd.manhattan() + this.moves) <  (that.brd.manhattan() + that.moves) ) 
				return -1;
			else if ( (this.brd.manhattan() + this.moves) > (that.brd.manhattan() + that.moves) )
				return 1;
			else
				return 0;
		}
		
		public String toString() {
			return this.brd.toString();
		}
	}
    
}
