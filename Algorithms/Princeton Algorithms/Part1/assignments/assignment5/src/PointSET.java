public class PointSET {

	private SET<Point2D> points;

	// construct an empty set of points
	public PointSET() {
		points = new SET<Point2D>();
	}

	// is the set empty?
	public boolean isEmpty() {
		return points.isEmpty();
	}

	// number of points in the set
	public int size() {
		return points.size();
	}

	// add the point p to the set (if it is not already in the set)
	public void insert(Point2D p) {
		points.add(p);
	}

	// does the set contain the point p?
	public boolean contains(Point2D p) {
		return points.contains(p);
	}

	// draw all of the points to standard draw
	public void draw() {
		StdDraw.clear();
		StdDraw.setPenColor(StdDraw.BLACK);

		for (Point2D point : points) {
			point.draw();
		}

		// display to screen all at once
		StdDraw.show(0);

		// reset the pen radius
		StdDraw.setPenRadius();
	}

	// all points in the set that are inside the rectangle
	public Iterable<Point2D> range(RectHV rect) {
		SET<Point2D> rectPoints = new SET<Point2D>();
	
		for (Point2D point : points) {
			if ( rect.contains(point) )
				rectPoints.add(point);
		}	
		return rectPoints;
	}

	// a nearest neighbor in the set to p; null if set is empty
	public Point2D nearest(Point2D p) {

		Point2D minPoint = null;
		if (points.isEmpty())
			return null;
		
		// Pick any point farther away than any point in our space.
		minPoint = new Point2D(2.1, 2.1);
		for (Point2D point : points) {
			if (p.distanceTo(point) < p.distanceTo(minPoint))
				minPoint = point;
		}

		return minPoint;
	}
}