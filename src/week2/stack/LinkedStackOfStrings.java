package week2.stack;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class LinkedStackOfStrings implements StackOfStrings {
    private class Node {
        String item;
        Node next;
    }

    private Node first = null;

    public boolean isEmpty() {
        return first == null;
    }

    @Override
    public void push(String item) {
        Node oldFirst = first;
        first = new Node();
        first.item = item;
        first.next = oldFirst;
    }

    @Override
    public String pop() {
        String item = first.item;
        first = first.next;
        return item;
    }

    public static void main(String[] args)
    {
        LinkedStackOfStrings stack = new LinkedStackOfStrings();
        while (!StdIn.isEmpty())
        {
            String s = StdIn.readString();
            if (s.equals("-")) StdOut.print(stack.pop());
            else               stack.push(s);
        }
    }
}
