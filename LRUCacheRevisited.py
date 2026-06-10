from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.user_map=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.user_map:
            self.user_map.move_to_end(key)
            return self.user_map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.user_map:
            self.user_map[key]=value
            self.user_map.move_to_end(key)
        else:
            self.user_map[key]=value
            self.user_map.move_to_end(key)
        if len(self.user_map) > self.capacity:
            self.user_map.popitem(last=False)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)