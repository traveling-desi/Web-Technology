public class KdTree {

	private int size;
	private Node root = null;

	// construct an empty set of points
	public KdTree() {
	}

	// is the set empty?
	public boolean isEmpty() {
		return (size == 0);
	}

	// number of points in the set
	public int size() {
		return this.size;		
	}

	
	
	// add the point p to the set (if it is not already in the set)
	public void insert(Point2D p) {
		Node parentNode = null;

		if (root == null) {
			root = new Node(p, new RectHV(0, 0, 1, 1), true);
			this.size++;
			return;
		}

//		System.out.println("Looking for Point " + p.toString());

		double px = p.x();
		double py = p.y();		
		
		parentNode = findInsertPoint(root, p, px, py);
		if (parentNode == null) {
			return;
		}

		insertNode(parentNode, p, px, py);

		this.size++;
		
//		System.out.println("SIZE IS =" + this.size);
	}

	
	
	// Insert the point p as child of parent node.
	private void insertNode(Node parentNode, Point2D p, double px, double py) {
		Node srchNode;
		double new_llx;
		double new_lly;
		double new_urx;
		double new_ury;
		double parent_rect_lly = parentNode.rect.ymin();
		double parent_rect_ury = parentNode.rect.ymax();
		double parent_rect_llx = parentNode.rect.xmin();
		double parent_rect_urx = parentNode.rect.xmax();
		if (parentNode.vert) {
			new_lly = parent_rect_lly;
			new_ury = parent_rect_ury;
			double parent_x = parentNode.p.x();
			if (px >= parent_x) {
				new_llx = parent_x;
				new_urx = parent_rect_urx;
				srchNode = new Node(p, new RectHV(new_llx, new_lly, new_urx, new_ury), false);
				parentNode.rt = srchNode;
			} else {
				new_llx = parent_rect_llx;
				new_urx = parent_x;
				srchNode = new Node(p, new RectHV(new_llx, new_lly, new_urx, new_ury), false);
				parentNode.lb = srchNode;
			}
		} else {
			new_llx = parent_rect_llx;
			new_urx = parent_rect_urx;
			double parent_y = parentNode.p.y();
			if (py >= parent_y) {
				new_lly = parent_y;
				new_ury = parent_rect_ury;
				srchNode = new Node(p, new RectHV(new_llx, new_lly, new_urx, new_ury), true);
				parentNode.rt = srchNode;
			} else {
				new_lly = parent_rect_lly;
				new_ury = parent_y;
				srchNode = new Node(p, new RectHV(new_llx, new_lly, new_urx, new_ury), true);
				parentNode.lb = srchNode;
			}
		}
	}

	// Find the parent node to insert the new node as child of.
	private Node findInsertPoint(Node srchNode, Point2D p, double px, double py) {
		Node parentNode = null;
		
		
//		while (srchNode != null) {
			parentNode = srchNode;

//			System.out.println("Looking in node Point " +
//			 srchNode.p.toString());

			//double srch_x = srchNode.p.x();
		
			double srch_x = srchNode.p.x();
			double srch_y = srchNode.p.y();
			
			if (px == srch_x && py == srch_y)
				return null;

			if (srchNode.vert) {
				if (px >= srch_x) {
					srchNode = srchNode.rt;
					// System.out.println(" Added RT +1" );
				} else {
					srchNode = srchNode.lb;
					// System.out.println(" Added LB +1" );
				}
			} else {
				if (py >= srch_y) {
					srchNode = srchNode.rt;
					// System.out.println(" Added RT +2" );
				} else {
					srchNode = srchNode.lb;
					// System.out.println(" Added LB +2" );
				}
			}
//		}
			if ( srchNode != null )
				return findInsertPoint(srchNode, p, px, py);
			else 
				return parentNode;
	}

	
	
	// does the set contain the point p?
	public boolean contains(Point2D p) {
		double px = p.x();
		double py = p.y();	
		
		return containsPoints(root, p, px, py);
	}

	private boolean containsPoints(Node s, Point2D p, double px, double py) {
		if (s == null)
			return false;
		
		if (s.p.equals(p))
			return true;

		
		if (s.vert) {
				if ( px >= s.p.x() ) {
					return containsPoints(s.rt, p, px, py);
				} else {
					return containsPoints(s.lb, p, px, py);
				}
		} else {
			if ( py >= s.p.y() ) {
				return containsPoints(s.rt, p, px, py);
			} else {
				return containsPoints(s.lb, p, px, py);
			}
		}
}

	// draw all of the points to standard draw
	public void draw() {
		StdDraw.clear();

		drawPoints(root);

		// display to screen all at once
		StdDraw.show(0);

		// reset the pen radius
		StdDraw.setPenRadius();
	}

	private void drawPoints(Node s) {
		if (s == null) {
			return;
		} else {
			if (s.vert) {
				StdDraw.setPenColor(StdDraw.RED);
				StdDraw.setPenRadius();
				StdDraw.line(s.p.x(), s.rect.ymin(), s.p.x(), s.rect.ymax());
			} else {
				StdDraw.setPenColor(StdDraw.BLUE);
				StdDraw.setPenRadius();
				StdDraw.line(s.rect.xmin(), s.p.y(), s.rect.xmax(), s.p.y());
			}
			drawPoints(s.rt);
			drawPoints(s.lb);
		}
		StdDraw.setPenColor(StdDraw.BLACK);
		StdDraw.setPenRadius(.01);
		s.p.draw();
	}

	// all points in the set that are inside the rectangle
	public Iterable<Point2D> range(RectHV rect) {
		
		SET<Point2D> rectPoints = new SET<Point2D>();
		
		rangePoints(root, rect, rectPoints);
		
		
//		for (Point2D p: rectPoints) {
//			System.out.println("X = " + p.x() + "Y = " + p.y());
//		}
		
		return rectPoints;

	}

	
	private void rangePoints(Node srchNode, RectHV rect, SET<Point2D> rectPoints ) {
		// TODO Auto-generated method stub
		
		if ( srchNode == null )
			return;
		
		RectHV srect = srchNode.rect;
		
//		StdDraw.setPenColor(StdDraw.RED);
//		srchNode.p.draw();
//        StdDraw.show(0);
		
		if ( srect.intersects(rect) ) {
			Point2D p = srchNode.p;
			if (rect.contains( p )) {
				rectPoints.add( p );
			}
			rangePoints(srchNode.lb, rect, rectPoints);
			rangePoints(srchNode.rt, rect, rectPoints);
		} else {
			return ;
		}
		
//		Point2D p1 = new Point2D(0.5, 0.1);
//		Point2D p2 = new Point2D(0.1, 0.5);
//		Point2D p3 = new Point2D(0.3, 0.2);
//		Point2D p4 = new Point2D(0.2, 0.3);
//		
//		rectPoints.add(p4);
//		rectPoints.add(p3);
//		rectPoints.add(p2);
//		rectPoints.add(p1);
		
	}

	// a nearest neighbor in the set to p; null if set is empty
	public Point2D nearest(Point2D p) {
		Point2D cPoint = new Point2D(100, 100);
		Point2D cp = nearestPoint(root, p, cPoint);
		if ( cp.equals(cPoint) ) {
			return null;
		} else {
			return cp;
		}
	}

	private Point2D nearestPoint(Node srchNode, Point2D p, Point2D cp) {
		// TODO Auto-generated method stub
		
		
		if ( srchNode == null )
			return cp;
		
//		StdDraw.setPenColor(StdDraw.RED);
//		srchNode.p.draw();
//        StdDraw.show(0);
		
		RectHV srect = srchNode.rect;
		
		if ( srect.distanceTo(p) > p.distanceTo(cp) )
			return cp;
		else {
			if (p.distanceTo(cp) > p.distanceTo(srchNode.p) )
				cp = srchNode.p;
			if ( srchNode.vert ) {
				double px = p.x();
				if (px >= srchNode.p.x() ) {
					cp = nearestPoint(srchNode.rt, p, cp);
					cp = nearestPoint(srchNode.lb, p, cp);
				} else {
					cp = nearestPoint(srchNode.lb, p, cp);
					cp = nearestPoint(srchNode.rt, p, cp);
				}
			} else {
				double py = p.y();
				if (py >= srchNode.p.y() ) {
					cp = nearestPoint(srchNode.rt, p, cp);
					cp = nearestPoint(srchNode.lb, p, cp);
				} else {
					cp = nearestPoint(srchNode.lb, p, cp);
					cp = nearestPoint(srchNode.rt, p, cp);
				}
			}
		}
		return cp;
	}

	private static class Node {
		private Point2D p; // the point
		private RectHV rect; // the axis-aligned rectangle corresponding to this node
		private Node lb; // the left/bottom subtree
		private Node rt; // the right/top subtree
		private boolean vert;

		public Node(Point2D p, RectHV rect, boolean vert) {
			this.p = p;
			this.rect = rect;
			this.vert = vert;
			this.lb = null;
			this.rt = null;
		}
	}
}