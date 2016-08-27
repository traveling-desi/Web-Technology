import java.util.Arrays;

public class Brute {

	public static void main(String[] args) {
		In in = new In(args[0]); // input file
		int n = in.readInt(); // N # of points
		
		Point[] pointArray = new Point[n];
		
        // rescale coordinates and turn on animation mode
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        StdDraw.show(0);
//        StdDraw.setPenRadius(0.01);  // make the points a bit larger

		for (int i = 0; i < n; i++) {		
			int a = in.readInt();
			int b = in.readInt();

			pointArray[i] = new Point(a,b);
//			System.out.println(pointArray[i].toString());
//			pointArray[i].draw();
		}

		Arrays.sort(pointArray);
	
//		for (int i = 0; i < n; i++) {	
//			System.out.println(pointArray[i].toString());
//		}
		
		
		
		for (int i = 0; i < n; i++) {
			Point node1 =  pointArray[i];
			node1.draw();
			for (int j = i+1; j < n; j++) {
				Point node2 =  pointArray[j];
				for (int k = j+1; k < n; k++) {
					Point node3 =  pointArray[k];
					for (int l = k+1; l < n; l++) {
						Point node4 =  pointArray[l];
						
						double slope1 = node1.slopeTo(node2);
						double slope2 = node1.slopeTo(node3);
						double slope3 = node1.slopeTo(node4);
						
						
						if (slope1 == slope2 && slope1 == slope3) {
							
//							System.out.println("i = " +i+ " j = " + j+" k = " +k+" l = " +l + " n = " + n);
//							System.out.println("slp 1 = " +slope1+ " slp 2 = " + slope2+" slp 3 = " +slope3);

//							node2.draw();
//							node3.draw();
//							node4.draw();
							
							node1.drawTo(node4);
							
							String node1Str = node1.toString();
							String node2Str = node2.toString();
							String node3Str = node3.toString();
							String node4Str = node4.toString();
							
							System.out.println(node1Str + " -> " + node2Str + " -> " + node3Str + " -> " + node4Str);
							

						}
					}
				}
			}
		}
		
        // display to screen all at once
        StdDraw.show(0);

        // reset the pen radius
        StdDraw.setPenRadius();

	}
}
