from collections import deque

class RecentCounter:
    # queue as member
    def __init__(self):
        # queue = []
        self.queue = deque()

    def ping(self, t: int) -> int:
        # peek first and if is not in the range between t-3000 and t poll
        # enqueue t 
        # return size
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)