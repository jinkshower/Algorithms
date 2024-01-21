package week2.queue;

public interface QueueOfStrings {
    void enqueue(String item);
    String dequeue();
    boolean isEmpty();
}
