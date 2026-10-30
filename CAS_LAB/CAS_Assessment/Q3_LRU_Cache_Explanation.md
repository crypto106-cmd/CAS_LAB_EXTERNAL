# Q3: Implement an LRU Cache — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Design a **Least Recently Used (LRU) Cache** that supports two operations:
- **GET(key)**: Return the value associated with the key, or -1 if the key doesn't exist.
- **PUT(key, value)**: Insert or update a key-value pair. If the cache is full, **evict the least recently used item** before inserting.

### What is an LRU Cache?
Imagine you have a bookshelf that can hold only 3 books. When you want to add a 4th book, you remove the book you haven't touched the longest. Every time you read or update a book, it becomes the "most recently used" one.

### What input do we receive?
- First line: `capacity` (max items) and `number of operations`.
- Each following line: either `GET key` or `PUT key value`.

### What output do we produce?
- For every `GET` operation, print the value or -1.
- `PUT` operations produce no output.

### Small Example
```
Cache capacity: 2
PUT 1 10    → cache: {1:10}
PUT 2 20    → cache: {1:10, 2:20}
GET 1       → returns 10, cache: {2:20, 1:10} (1 is now most recent)
PUT 3 30    → cache full! Evict least recent (key 2). cache: {1:10, 3:30}
GET 2       → returns -1 (evicted)
GET 3       → returns 30
```

---

## B. Algorithm and Approach

### Approach: OrderedDict

Python's `OrderedDict` from the `collections` module maintains the **insertion order** of keys. It also provides:
- `move_to_end(key)`: Moves a key to the end (most recently used) in O(1).
- `popitem(last=False)`: Removes the first item (least recently used) in O(1).

### Step-by-Step Logic:
1. Create an `OrderedDict` with a given capacity.
2. **GET operation**:
   - If key exists: move it to the end (mark as most recently used) and return its value.
   - If key doesn't exist: return -1.
3. **PUT operation**:
   - If key already exists: update its value and move it to the end.
   - If key doesn't exist:
     - If cache is full: remove the first item (least recently used) using `popitem(last=False)`.
     - Insert the new key-value pair (it goes at the end automatically).

### Why OrderedDict?
- It combines a hash map (for O(1) lookup) with a doubly linked list (for maintaining order).
- Both GET and PUT are O(1) — exactly what the problem requires.

---

## C. Complete Python Code

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

first_line = input().split()
capacity = int(first_line[0])
num_operations = int(first_line[1])

lru = LRUCache(capacity)

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
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
2 6
PUT 1 10
PUT 2 20
GET 1
PUT 3 30
GET 2
GET 3
```
**Expected Output:**
```
10
-1
30
```
**Explanation:**
- `PUT 1 10` → cache: {1:10}
- `PUT 2 20` → cache: {1:10, 2:20}
- `GET 1` → found, output **10**, move 1 to end → cache: {2:20, 1:10}
- `PUT 3 30` → cache full (capacity 2). Evict least recent = key 2. → cache: {1:10, 3:30}
- `GET 2` → not found → output **-1**
- `GET 3` → found → output **30**

### Test Case 2
**Input:**
```
1 5
PUT 1 100
GET 1
PUT 2 200
GET 1
GET 2
```
**Expected Output:**
```
100
-1
200
```
**Explanation:**
- `PUT 1 100` → cache: {1:100}
- `GET 1` → found → output **100**
- `PUT 2 200` → cache full (capacity 1). Evict key 1. → cache: {2:200}
- `GET 1` → not found → output **-1**
- `GET 2` → found → output **200**

---

## E. Detailed Code Explanation

### Line: `from collections import OrderedDict`
- Imports `OrderedDict`, a dictionary that remembers the order in which keys were inserted.
- This is the foundation of our LRU Cache.

### Line: `class LRUCache:`
- Defines a class named `LRUCache` to encapsulate the cache logic.
- A class groups data (the cache dictionary, capacity) and methods (get, put) together.

### Line: `def __init__(self, capacity):`
- The **constructor** — called automatically when we create an `LRUCache` object.
- `self` refers to the current object being created.
- `capacity` sets the maximum number of items the cache can hold.

### Line: `self.cache = OrderedDict()`
- Creates the internal storage for the cache.
- `self.cache` is an instance variable accessible by all methods of the class.

### Line: `self.cache.move_to_end(key)`
- Moves the given key to the **end** of the OrderedDict.
- The end represents the "most recently used" position.
- This is an O(1) operation.

### Line: `self.cache.popitem(last=False)`
- Removes the **first** item from the OrderedDict.
- `last=False` means remove from the beginning (least recently used).
- `last=True` would remove from the end (most recently used).

### Line: `len(self.cache) >= self.capacity`
- Checks if the cache is at full capacity.
- `len()` returns the number of items in the OrderedDict.

---

## F. Python Syntax Explanation

### `class`
- Defines a blueprint for creating objects.
- Contains attributes (variables) and methods (functions).
- `class LRUCache:` creates a class named LRUCache.

### `__init__` (Constructor)
- A special method called automatically when an object is created.
- Used to initialize the object's attributes.
- Always has `self` as the first parameter.

### `self`
- Refers to the current instance of the class.
- Used to access instance variables and methods.
- `self.capacity` is the capacity for THIS specific cache object.

### `OrderedDict`
- A dictionary subclass that remembers insertion order.
- Key methods: `move_to_end(key)`, `popitem(last=True/False)`.
- Regular `dict` in Python 3.7+ also preserves insertion order, but `OrderedDict` provides `move_to_end()`.

### `split()`
- Splits a string by whitespace and returns a list.
- `"PUT 1 10".split()` → `["PUT", "1", "10"]`

### `int()`
- Converts a string to an integer.
- `int("10")` → `10`

---

## G. Why This Method and Not Another Method?

### Why OrderedDict?
- Provides both O(1) lookup (like a regular dictionary) and O(1) order manipulation (`move_to_end`, `popitem`).
- Internally uses a hash table + doubly linked list.
- Perfect for LRU Cache.

### Alternative 1: Dictionary + Doubly Linked List (Manual)
- Build a doubly linked list manually with a dictionary mapping keys to nodes.
- This is what `OrderedDict` does internally.
- More code, harder to debug, same performance.
- **Good for understanding** the internals, but unnecessary when Python provides `OrderedDict`.

### Alternative 2: Dictionary + List
- Use a list to track usage order.
- Moving an item in a list is O(n), not O(1).
- **Rejected** because it doesn't meet the O(1) requirement.

### Alternative 3: Dictionary + Timestamp
- Store a timestamp with each entry and find the oldest when evicting.
- Finding the minimum timestamp is O(n).
- **Rejected** because GET and PUT would not be O(1).

### Advantages of Our Approach:
- Clean, minimal code.
- Leverages Python's standard library.
- O(1) for all operations.
- Easy to explain.

---

## H. Time and Space Complexity

### Time Complexity: O(1) per operation
- `GET`: Dictionary lookup O(1) + `move_to_end` O(1) = O(1).
- `PUT`: Dictionary lookup O(1) + possible `popitem` O(1) + insertion O(1) = O(1).
- Total for all operations: O(number of operations).

### Space Complexity: O(capacity)
- The OrderedDict stores at most `capacity` key-value pairs.
- No additional data structures are used.

---

## I. Faculty Viva Questions and Answers

### Q1: What does LRU stand for?
**A:** Least Recently Used. It's a cache eviction policy that removes the item that hasn't been accessed for the longest time when the cache is full.

### Q2: Why is O(1) important for cache operations?
**A:** Caches are used in performance-critical systems (CPU caches, web browsers, databases). If cache operations were slow, they would defeat the purpose of caching. O(1) means the cache responds in constant time regardless of how many items it holds.

### Q3: How does OrderedDict maintain order?
**A:** Internally, it uses a **doubly linked list** along with a **hash table**. The hash table gives O(1) lookup, and the linked list maintains insertion/access order with O(1) reordering.

### Q4: What happens if we PUT a key that already exists?
**A:** We update its value and move it to the end (most recently used). We do NOT add a duplicate entry. The cache size remains the same.

### Q5: What is the difference between OrderedDict and a regular dict?
**A:** In Python 3.7+, regular `dict` preserves insertion order but does NOT provide `move_to_end()` or `popitem(last=False)`. `OrderedDict` provides these methods, making it suitable for LRU Cache.

### Q6: What is cache eviction?
**A:** When the cache is full and a new item needs to be added, an existing item must be removed ("evicted"). LRU evicts the least recently used item.

### Q7: Can we implement LRU Cache without OrderedDict?
**A:** Yes, by manually implementing a doubly linked list + hash map. The hash map maps keys to linked list nodes. On access, we move the node to the head. On eviction, we remove the tail. This is the classic implementation taught in DSA.

### Q8: What other cache eviction policies exist?
**A:** FIFO (First In First Out), LFU (Least Frequently Used), MRU (Most Recently Used), and Random Replacement. Each has different use cases depending on access patterns.

### Q9: Where is LRU Cache used in real life?
**A:** CPU caches, web browser caches, database query caches, operating system page replacement, CDN (Content Delivery Network) caches.

### Q10: What is the role of `self` in the class?
**A:** `self` is a reference to the current object instance. It allows each object to have its own copy of `capacity` and `cache`. Without `self`, the variables would be local to the method and lost after the method returns.

### Q11: What does `popitem(last=False)` do?
**A:** It removes and returns the first (oldest) key-value pair from the OrderedDict. With `last=True` (default), it removes the last (newest) pair.

### Q12: What is the time complexity if we used a list instead of OrderedDict?
**A:** Finding and removing an element from a list is O(n), so GET and PUT would become O(n) instead of O(1). This would be too slow for 200,000 operations.

---

## J. VS Code Execution

### Step-by-Step:
1. Open VS Code.
2. Open the `CAS_Assessment` folder.
3. Open `Q3_LRU_Cache.py`.
4. Open the terminal: `` Ctrl+` ``
5. Run: `python Q3_LRU_Cache.py`
6. Enter input line by line.

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q3_LRU_Cache.py
2 6
PUT 1 10
PUT 2 20
GET 1
PUT 3 30
GET 2
GET 3
10
-1
30
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q3_LRU_Cache.py
1 5
PUT 1 100
GET 1
PUT 2 200
GET 1
GET 2
100
-1
200
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | LRU Eviction using OrderedDict |
| **Data Structure** | OrderedDict (hash map + doubly linked list) |
| **Core Logic** | 1. GET: lookup + move to end. 2. PUT: if exists, update + move to end. 3. If full, evict first item. 4. Insert at end. |
| **Memory Trick** | "End = recent, Front = evict, OrderedDict does both in O(1)" |
| **One Sentence** | Use Python's OrderedDict to maintain access order, moving items to the end on access and evicting from the front when full. |
