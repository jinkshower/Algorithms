package assignment2;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private Node<Item> first, last;
    private int n;
    // construct an empty deque
    public Deque() {
    }

    // is the deque empty?
    public boolean isEmpty() {
        return n == 0;
    }

    // return the number of items on the deque
    public int size() {
        return n;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) throw new IllegalArgumentException();
        if (isEmpty()) {
            first = new Node<>(item);
            last = first;
        } else {
            Node<Item> node = new Node<>(item);
            first.prev = node;
            node.next = first;
            first = node;
        }
        n++;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) throw new IllegalArgumentException();
        if (isEmpty()) {
            last = new Node<>(item);
            first = last;
        } else {
            Node<Item> node = new Node<>(item);
            last.next = node;
            node.prev = last;
            last = node;
        }
        n++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) throw new NoSuchElementException();
        Item item = first.item;
        first = first.next;
        n--;
        return item;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (isEmpty()) throw new NoSuchElementException();
        Item item = last.item;
        last = last.prev;
        n--;
        return item;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new DequeIterator(first);
    }

    // unit testing (required)
    public static void main(String[] args) {
        Deque<Integer> deq2 = new Deque<Integer>();

        System.out.println("deq2: " + deq2.toString());
        System.out.println("size: " + deq2.size());

        deq2.addFirst(1);
        deq2.addFirst(2);
        deq2.addFirst(3);
        deq2.addFirst(4);
        deq2.addFirst(5);

        System.out.println(deq2.removeLast());
        System.out.println(deq2.removeFirst());
        System.out.println(deq2.removeFirst());
        System.out.println(deq2.removeLast());
        System.out.println(deq2.removeLast());

        deq2.addFirst(1);
        deq2.addLast(2);
        deq2.addFirst(3);
        deq2.addLast(4);

        Iterator<Integer> itr = deq2.iterator();

    }

    private class DequeIterator implements Iterator<Item> {

        private Node<Item> current;

        public DequeIterator(Node<Item> first) {
            current = first;
        }
        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    private static class Node<Item> {
        Item item;
        Node<Item> prev;
        Node<Item> next;

        Node(Item item) {
            this.item = item;
            this.next = null;
            this.prev = null;
        }
    }
}
