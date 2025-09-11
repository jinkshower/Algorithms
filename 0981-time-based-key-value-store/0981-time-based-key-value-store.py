class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            found = self.store[key]
            found.append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        found = self.store[key]

        l, r = 0, len(found) - 1
        val = ""
        while (l <= r):
            m = (l + r) // 2

            if found[m][1] <= timestamp:
                # search right
                val = found[m][0]
                l = m + 1
            else:
                r = m - 1
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)