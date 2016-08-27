
public class Subset {
	
	   public static void main(String[] args)  {
		   
		   String num = args[0];
		   RandomizedQueue<String> rq = new RandomizedQueue<String>();
		   
		   //System.out.println("I am here1");
		   String[] inp = StdIn.readAllStrings();
		   //System.out.println("I am here2");
		   //System.out.println(inp);
		   
		   for (int i = 0; i < inp.length; i++) {
			   rq.enqueue(inp[i]);
			   //System.out.println("item is " + inp[i]);
		   }
		   //System.out.println("I am here");
		   for (int i = 0; i < Integer.parseInt(num); i++)
			   System.out.println(rq.dequeue());
	   }
}
