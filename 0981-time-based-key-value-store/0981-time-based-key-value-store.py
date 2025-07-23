        
# set foo bar1 1 
# set foo bar2 2
# set foo bar3 3

# timestamp_prev <= timestamp 

# { "foo" : [ (Pair - bar1, 1), (Pair - bar2, 2), (Pair - bar3, 3), ............] 

# get foo 2
# retur bar2

# memorize index where condition has fulfilled.
# found 

# time
# set - nlogn 
# get - logn 

# space
# O(n)
class Pair:

    def __init__(self, name: str, timestamp: int) -> None:
        self.name = name
        self.timestamp = timestamp

class TimeMap:

    def __init__(self):
        # hashMap with its value - sorted list
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key is present
        #    append new Pair
        #    sort based on timestamp
        if key in self.hashMap:
            found = self.hashMap[key]
            found.append(Pair(value, timestamp))
        else: 
            self.hashMap[key] = [Pair(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # if key is present
        #    binary search and find prev <= timestamp
        if key not in self.hashMap:
            return ""
        values = self.hashMap[key]

        l, r = 0, len(values) - 1
        found = -1
        while l <= r:
            m = (l + r) // 2

            if values[m].timestamp <= timestamp:
                found = m
                # search right
                l = m + 1
            else:
                r = m - 1
        return values[found].name if found != -1 else ""
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)