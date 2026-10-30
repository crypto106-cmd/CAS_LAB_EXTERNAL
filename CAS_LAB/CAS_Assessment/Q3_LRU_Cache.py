# Q3: Implement an LRU Cache
# Algorithm: OrderedDict (Hash Map + Doubly Linked List internally)
# Time Complexity: O(1) per GET/PUT | Space Complexity: O(capacity)

from collections import OrderedDict

class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation.
    When the cache is full and a new item is added,
    the least recently used item is evicted.
    """
    
    def __init__(self, capacity):
        """Initialize the cache with given capacity."""
        self.capacity = capacity
        self.cache = OrderedDict()  # Maintains insertion order
    
    def get(self, key):
        """
        Get the value for a key.
        Returns -1 if key does not exist.
        If key exists, mark it as most recently used.
        """
        if key not in self.cache:
            return -1
        
        # Move the accessed key to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """
        Insert or update a key-value pair.
        If key already exists, update its value and mark as most recently used.
        If cache is full, remove the least recently used item first.
        """
        if key in self.cache:
            # Key exists: update value and move to end
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            # Key does not exist: check if cache is full
            if len(self.cache) >= self.capacity:
                # Remove the first item (least recently used)
                self.cache.popitem(last=False)
            # Insert the new key-value pair at the end
            self.cache[key] = value


# ---- Main Program ----
# Read capacity and number of operations
first_line = input().split()
capacity = int(first_line[0])
num_operations = int(first_line[1])

# Create the LRU Cache
lru = LRUCache(capacity)

# Process each operation
for i in range(num_operations):
    line = input().split()
    operation = line[0]
    
    if operation == "GET":
        key = int(line[1])
        result = lru.get(key)
        print(result)
    
    elif operation == "PUT":
        key = int(line[1])
        value = int(line[2])
        lru.put(key, value)
