import java.util.Arrays;

public class Fast {
	public static void main(String[] args) {
		In in = new In(args[0]); // input file
		int n = in.readInt(); // N # of points

		Point[] pointArray1 = new Point[n];
		Point[] pointArray2 = new Point[n];
		ST<String, String> st = new ST<String, String>();

		// rescale coordinates and turn on animation mode
		StdDraw.setXscale(0, 32768);
		StdDraw.setYscale(0, 32768);
		StdDraw.show(0);
		// StdDraw.setPenRadius(0.01); // make the points a bit larger

		for (int i = 0; i < n; i++) {
			int a = in.readInt();
			int b = in.readInt();

			pointArray1[i] = new Point(a, b);
			pointArray2[i] = pointArray1[i];
		}

		Arrays.sort(pointArray1);

		for (int i = 0; i < n; i++) {
			Point node1 = pointArray1[i];
			Arrays.sort(pointArray2, node1.SLOPE_ORDER);
			node1.draw();

			for (int j = 1; j < n; j++) {

				Point node2 = pointArray2[j];

				double slope1 = node1.slopeTo(node2);

				int k = 1;
				while (j + k < pointArray2.length
						&& node1.slopeTo(pointArray2[j + k]) == slope1) {
					++k;
				}

				if (k > 2) {

					Point[] tempPointArray = new Point[k + 1];
					String[] nodeStr = new String[k];
					String printStr = "";

					for (int l = 0; l < k; l++) {
						tempPointArray[l] = pointArray2[j + l];
					}
					tempPointArray[k] = node1;

					Arrays.sort(tempPointArray);

					for (int l = 0; l < k; l++) {
						nodeStr[l] = tempPointArray[l].toString();
						printStr += nodeStr[l] + " -> ";
					}
					printStr += tempPointArray[k].toString();
					printStr += "";

					if (!st.contains(printStr)) {
						System.out.println(printStr);
						tempPointArray[0].drawTo(tempPointArray[k]);
						st.put(printStr, "");
					}

					j = j + k - 1;

					tempPointArray = null;
					nodeStr = null;
					printStr = null;
				}
			}
		}
		// display to screen all at once
		StdDraw.show(0);

		// reset the pen radius
		StdDraw.setPenRadius();

	}
}
