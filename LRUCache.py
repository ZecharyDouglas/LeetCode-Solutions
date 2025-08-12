from collections import OrderedDict 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = abs(capacity)
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        #when checking for a key make sure to use "key in self.cache" because if the key has falsy values like 
        # "" , 0 , False or None it will fail. 
        if key in self.cache:
            self.cache.move_to_end(key , last=False)
            return self.cache.get(key)
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key , last=False)
        elif key not in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key , last=False)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=True)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)