package week2.stack;

public class ResizingArrayStackOfStrings implements StackOfStrings {

    private String[] s;
    private int N = 0;

    public ResizingArrayStackOfStrings() {
        this.s = new String[1];
    }

    @Override
    public boolean isEmpty() {
        return N == 0;
    }

    @Override
    public void push(String item) {
        if (N == s.length) resize(2 * s.length);
        s[N++] = item;
    }

    @Override
    public String pop() {
        String item = s[--N];
        s[N] = null;
        if (N > 0 && N == s.length / 4) {
            resize(s.length / 2);
        }
        return s[--N];
    }

    private void resize(int capacity) {
        String[] copy = new String[capacity];
        for (int i = 0; i < N; i++) {
            copy[i] = s[i];
        }
        s = copy;
    }
}
