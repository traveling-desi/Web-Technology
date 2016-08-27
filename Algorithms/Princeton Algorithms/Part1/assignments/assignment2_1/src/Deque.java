
import java.lang.NullPointerException;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

	private class Node {
		Item item;
		Node next;
		Node prev;

		public Node() {

		}
	}

	private Node first, last = null;
	private int size = 0;

	// construct an empty deque
	public Deque() {

	}

	// is the deque empty?
	public boolean isEmpty() {
		return (size == 0);

	}

	// return the number of items on the deque
	public int size() {
		return size;

	}

	// insert the item at the front
	public void addFirst(Item item) {
		if (checkItem(item)) {
			Node oldfirst = first;
			first = new Node();

			if (last == null) {
				last = first;
			}

			if (oldfirst != null) {
				oldfirst.prev = first;
			}

			first.item = item;
			first.next = oldfirst;
			first.prev = null;

			size++;
		}
	}

	private boolean checkItem(Item item) {
		if (item == null) {
			throw new NullPointerException("Adding null item: NOT ALLOWED");
		} else {
			return true;
		}
	}

	// insert the item at the end
	public void addLast(Item item) {
		if (checkItem(item)) {
			Node oldlast = last;
			last = new Node();

			if (first == null) {
				first = last;
			}

			if (oldlast != null) {
				oldlast.next = last;
			}

			last.item = item;
			last.next = null;
			last.prev = oldlast;

			size++;
		}
	}

	// delete and return the item at the front
	public Item removeFirst() {
		if (checkValidItem()) {
			Item item = first.item;

			Node oldfirst = first;

			first = first.next;

			if (first != null) {
				first.prev = null;
			} else {
				last = null;
			}

			oldfirst.next = null;
			oldfirst.item = null;

			size--;

			return item;
		} else {
			return null;
		}
	}

	private boolean checkValidItem() {
		// TODO Auto-generated method stub
		if (isEmpty()) {
			throw new NoSuchElementException(
					"Removing from empty list: NOT ALLOWED");
		}
		return true;
	}

	// delete and return the item at the end
	public Item removeLast() {
		if (checkValidItem()) {
			Item item = last.item;

			Node oldlast = last;

			last = last.prev;

			if (last != null) {
				last.next = null;
			} else {
				first = null;
			}

			oldlast.prev = null;
			oldlast.item = null;

			size--;

			return item;
		} else {
			return null;
		}
	}

	// return an iterator over items in order from front to end
	public Iterator<Item> iterator() {
		return new ListIterator();
	}

	private class ListIterator implements Iterator<Item> {
		private Node current = first;

		public boolean hasNext() {
			return current != null;
		}

		public void remove() {
			throw new UnsupportedOperationException();
		}

		public Item next() {
			if (!hasNext())
				throw new NoSuchElementException();
			Item item = current.item;
			current = current.next;
			return item;
		}
	}

	// unit testing
	public static void main(String[] args) {

	}
}
