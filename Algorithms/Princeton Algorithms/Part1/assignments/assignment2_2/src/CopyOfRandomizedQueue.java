import java.util.Iterator;
import java.util.NoSuchElementException;



/// Use resizing array to implement. Constant amortized time.
public class CopyOfRandomizedQueue<Item> implements Iterable<Item> {
	
	private Item[] itemList;
	int ptr_hd = -1;
	int ptr_tail = -1;
	int size = 0;
	
	// construct an empty randomized queue   
	@SuppressWarnings("unchecked")
	public CopyOfRandomizedQueue() {	
		itemList = (Item[]) new Object[1];
	}
	
	// is the queue empty?
	   public boolean isEmpty() {
		return (size == 0);
		   
	   }
	   
	// return the number of items on the queue
	   public int size()  {
		return size;
		   
	   }
	   
	// add the item
	   public void enqueue(Item item)  {
		   checkItem(item);
		   if (itemList.length == size) {
			   doublesize(2 * itemList.length);
		   }
		   if (ptr_tail == ptr_hd && size == 0) {
			   // first item in empty queue.
			   itemList[ptr_tail] = item;
		   } else if (ptr_tail != itemList.length) {
			   itemList[ptr_tail++] = item;
		   } else {
			   ptr_tail = 0;
			   itemList[ptr_tail++] = item;
		   }
		   size++;

	   }
	   
		private boolean checkItem(Item item) {
			if(item == null) {
				throw new NullPointerException("Adding null item: NOT ALLOWED");
			} else {
				return true;
			}
	   }
	   
	   
	private void doublesize(int capacity) {
		// TODO Auto-generated method stub
		@SuppressWarnings("unchecked")
		Item[] copy = (Item[]) new Object[capacity];
		
			// ptr_tail = ptr_hd should happen only hwne size = 1
			if (ptr_tail >= ptr_hd) {
				for (int i = 0; i <= ptr_tail; i++)
					copy[i] = itemList[i];
			} else {
				// folding case. tail has wrapped around and starting from 0 again
				for (int i = ptr_hd; i < capacity/2; i++)
					copy[i] = itemList[i];
				for (int i = 0; i <= ptr_tail; i++)
					copy[i + capacity/2] = itemList[i];
			}
		
		itemList = copy;
	}

	// delete and return a random item
	   public Item dequeue() {
		   if (checkValidItem()) {
			   if(itemList.length == 4*size) {
				   halfsize(itemList.length/2);
			   }		   
			   int temp_ptr = 0;
			   Item item;
			   if (ptr_tail > ptr_hd) {
				   temp_ptr = StdRandom.uniform(ptr_hd, ptr_tail);
				   item = itemList[temp_ptr];
				   itemList[temp_ptr] = itemList[ptr_hd];
				   itemList[ptr_tail] = null;
				   ptr_tail --;
			   } else if (ptr_hd > ptr_tail)  {
				   temp_ptr = StdRandom.uniform(ptr_tail, ptr_hd);
				   item = itemList[ptr_hd];
				   itemList[temp_ptr] = itemList[ptr_hd];
				   itemList[ptr_hd] = null;
				   ptr_hd --;
				   
			   } else {
				   /// Ptr_tail = ptr_head. I.e only one element in the queue. Return it
				   item = itemList[ptr_hd];
			   }   
			   size --;
			   return item;
		   } else {
			   return null;
		   }
		   
	   }
	   
	   private void halfsize(int i) {
		// TODO Auto-generated method stub
		
	}

	private boolean checkValidItem() {
		// TODO Auto-generated method stub
		if(isEmpty()) {
			throw new NoSuchElementException("Removing from empty list: NOT ALLOWED");
		}
		return true;
	}
	   
	   
	   
	// return (but do not delete) a random item
	   public Item sample()  {
		  int temp_ptr = StdRandom.uniform(1, ptr_tail+1);
		  return itemList[temp_ptr];
	   }
	   
	// return an independent iterator over items in random order
	   public Iterator<Item> iterator() {
		   return new ArrayIterator();
	   }
	   
	   public class ArrayIterator implements Iterator<Item> {
				private int ptr_itr = 0;
				public boolean hasNext() { return ptr_itr != itemList.length; }
				public void remove()      { throw new UnsupportedOperationException();  }
				public Item next ()
				{
					return itemList[ptr_itr++];
				}
			}
		     
	// unit testing
	   public static void main(String[] args)  {
		   
	   }
	}