import java.util.Comparator;


public class Point implements Comparable<Point> {

	private  class slope_order implements Comparator<Point> {
		public int compare(Point a, Point b) {
			
			// if a less than b return 1
			// if a equal to b return 0
			// if a greater than b return -1
			
			if (slopeTo(a) < slopeTo(b)) {
				// Descending
				//return 1;
				// Ascending
				return -1;
				
			} else if (slopeTo(a) > slopeTo(b)) {
				// Descending
				//return -1;
				// Ascending
				return 1;
			} else {
				return 0;
			}
		}
	}

	// compare points by slope to this point
	public final Comparator<Point> SLOPE_ORDER = new slope_order();

	private int x; // x coordinate
	private int y; // y coordinate

	// construct the point (x, y)
	public Point(int x, int y) {
		/* DO NOT MODIFY */
		this.x = x;
		this.y = y;
	}

	// draw this point
	public void draw() {
		/* DO NOT MODIFY */
		StdDraw.point(x, y);
	}

	// draw the line segment from this point to that point
	public void drawTo(Point that) {
		/* DO NOT MODIFY */
		StdDraw.line(this.x, this.y, that.x, that.y);
	}

	// string representation
	public String toString() {
        /* DO NOT MODIFY */
        return "(" + x + ", " + y + ")";
	}

	// is this point lexicographically smaller than that point?
	public int compareTo(Point that) {
		if (this.y < that.y ) {
			// Ascending
			return -1;
			// Descending
			// return 1;	
		} else if (this.y > that.y) {
			// Ascending
			return 1;
			// Descending
			// return -1;	
		} else {
			if (this.x < that.x) {
				// Ascending
				return -1;
				// Descending
				// return 1;	
			} else if (this.x > that.x) {
				// Ascending
				return 1;
				// Descending
				// return -1;	
			} else {
				return 0;
			}
		}
	}

	// the slope between this point and that point
	public double slopeTo(Point that) {
		double slope;
		
		if (this.compareTo(that) == 0) {
			slope = (Double.POSITIVE_INFINITY * -1);
		} else if (this.x == that.x) {
			slope = Double.POSITIVE_INFINITY;
		} else if (this.y == that.y) {
			slope = 0.0;
		} else {
			slope = (double) (that.y - this.y)/(that.x - this.x);
//			System.out.println("Slope = " + slope);
		}
		return slope;
	}

}