import java.util.Iterator;
import java.util.NoSuchElementException;

/// Use resizing array to implement. Constant amortized time.
public class RandomizedQueue<Item> implements Iterable<Item> {

	private Item[] itemList;
	private int ptr_tail = -1;
	private int size = 0;

	// construct an empty randomized queue
	@SuppressWarnings("unchecked")
	public RandomizedQueue() {
		itemList = (Item[]) new Object[1];
	}

	// is the queue empty?
	public boolean isEmpty() {
		return (size == 0);

	}

	// return the number of items on the queue
	public int size() {
		return size;

	}

	// add the item
	public void enqueue(Item item) {
		checkItem(item);
		if (itemList.length == size) {
			resize(2 * itemList.length);
		}
		itemList[++ptr_tail] = item;
		size++;

	}

	private boolean checkItem(Item item) {
		if (item == null) {
			throw new NullPointerException("Adding null item: NOT ALLOWED");
		} else {
			return true;
		}
	}

	private void resize(int capacity) {
		// TODO Auto-generated method stub
		@SuppressWarnings("unchecked")
		Item[] copy = (Item[]) new Object[capacity];

		for (int i = 0; i <= ptr_tail; i++)
			copy[i] = itemList[i];

		itemList = copy;
	}

	// delete and return a random item
	public Item dequeue() {
		checkValidItem();
		if (itemList.length == 4 * size) {
			resize(itemList.length / 2);
		}

		Item item;
		
		int temp_ptr = StdRandom.uniform(0, ptr_tail + 1);
		item = itemList[temp_ptr];
		itemList[temp_ptr] = itemList[ptr_tail];
		itemList[ptr_tail] = null;
		ptr_tail--;
		size--;
		return item;

	}

	private boolean checkValidItem() {
		// TODO Auto-generated method stub
		if (isEmpty()) {
			throw new NoSuchElementException(
					"Removing from empty list: NOT ALLOWED");
		}
		return true;
	}

	// return (but do not delete) a random item
	public Item sample() {
		checkValidItem();
		int temp_ptr = StdRandom.uniform(0, ptr_tail + 1);
		return itemList[temp_ptr];
	}

	// return an independent iterator over items in random order
	public Iterator<Item> iterator() {
		return new ArrayIterator();
	}

	private class ArrayIterator implements Iterator<Item> {
		private int ptr_itr = -1;
		final int[] itemindex = new int[size];

		public boolean hasNext() {
			return ptr_itr != (size -1);
		}

		public void remove() {
			throw new UnsupportedOperationException();
		}

		public Item next() {
			if (!hasNext())
				throw new NoSuchElementException();
			return itemList[itemindex[++ptr_itr]];
		}

		public ArrayIterator() {
			for (int i = 0; i < size; i++) {
				itemindex[i] = i;
			}
			StdRandom.shuffle(itemindex);
		}
	}

	// unit testing
	public static void main(String[] args) {

	}
}