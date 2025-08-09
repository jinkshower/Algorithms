# doubly linked list
class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # map
        self.cache = {}

        #dummy
        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next, self.most.prev = self.most, self.least

    # remove node from linked list
    def remove(self, node):
        # prev -> <- node  -> <- next
        # prev -----------------> next
        # prev <---------------- next  
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    def insert(self, node):
        # prev <- -> most
        # prev <- -> node <- -> most
        prev = self.most.prev
        node.prev, node.nxt = prev, self.most
        prev.next = self.most.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove node 
            self.insert(self.cache[key]) # and insert it as self.most
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # don't need to really update existing node.
        # just create new one
        if key in self.cache:
            self.remove(self.cache[key])
        newOne = Node(key, value)
        self.cache[key] = newOne
        self.insert(newOne)

        # evict if capacity is full
        if len(self.cache) > self.cap:
            # remove least from list and map
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)