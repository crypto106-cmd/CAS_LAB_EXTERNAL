# Q5: Top K Frequent Elements — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Given an array of integers and a number `k`, find the `k` elements that appear **most frequently** in the array.

### What input do we receive?
- First line: `n` (number of elements) and `k` (how many top frequent elements to find).
- Second line: `n` integers separated by spaces.

### What output do we produce?
- The `k` most frequent elements separated by spaces.
- If two elements have the same frequency, any order is accepted.

### Small Example
```
Array: [1, 1, 1, 2, 2, 3], k = 2
Frequencies: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time.
Top 2 frequent: 1 and 2.
Output: 1 2
```

---

## B. Algorithm and Approach

### Approach: Hash Map + Heap (nlargest)

1. **Count frequencies**: Use a `Counter` (dictionary) to count how many times each element appears.
2. **Find top k**: Use `heapq.nlargest(k, ...)` to get the k elements with the highest frequencies.

### How does `heapq.nlargest` work?
- It maintains a **min heap** of size k internally.
- It scans through all elements:
  - If the heap has fewer than k elements, add the current element.
  - If the current element is larger than the smallest in the heap, replace the smallest.
- After processing all elements, the heap contains the k largest values.
- Time: O(n log k) — for each of n elements, heap operations take O(log k).

### Why this approach?
- Counting is O(n).
- Finding top k using `nlargest` is O(n log k).
- Total: O(n log k) — matches the expected complexity.

---

## C. Complete Python Code

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    top_k = heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])
    return top_k

first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])

nums = list(map(int, input().split()))

result = top_k_frequent(nums, k)
print(' '.join(map(str, result)))
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
6 2
1 1 1 2 2 3
```
**Expected Output:**
```
1 2
```
**Explanation:**
- Frequencies: {1: 3, 2: 2, 3: 1}
- Top 2 most frequent: 1 (freq 3) and 2 (freq 2)
- Output: `1 2`

### Test Case 2
**Input:**
```
9 3
4 4 1 1 1 2 2 2 2
```
**Expected Output:**
```
2 1 4
```
**Explanation:**
- Frequencies: {4: 2, 1: 3, 2: 4}
- Top 3 most frequent: 2 (freq 4), 1 (freq 3), 4 (freq 2)
- Output: `2 1 4`

---

## E. Detailed Code Explanation

### Line: `import heapq`
- Imports Python's heap queue module.
- Provides `nlargest()`, `nsmallest()`, `heappush()`, `heappop()`.
- Python's heapq implements a **min heap**.

### Line: `from collections import Counter`
- `Counter` is a specialized dictionary for counting hashable objects.
- `Counter([1,1,2,3])` → `{1: 2, 2: 1, 3: 1}`

### Line: `freq = Counter(nums)`
- Counts the frequency of each number in the array.
- Returns a dictionary-like object with elements as keys and counts as values.

### Line: `top_k = heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])`
- `heapq.nlargest(k, iterable, key)` returns the `k` largest elements from the iterable.
- `freq.keys()` provides all unique numbers.
- `key=lambda x: freq[x]` tells it to compare by frequency value, not by the number itself.
- Returns a list of k elements sorted by frequency (highest first).

### Line: `nums = list(map(int, input().split()))`
- `input().split()` reads a line and splits by spaces → list of strings.
- `map(int, ...)` converts each string to an integer.
- `list(...)` converts the map object to a list.

### Line: `print(' '.join(map(str, result)))`
- `map(str, result)` converts each integer back to a string.
- `' '.join(...)` joins them with spaces.
- Produces output like `"1 2"`.

---

## F. Python Syntax Explanation

### `heapq` module
- Provides heap-based priority queue operations.
- `heapq.nlargest(k, iterable, key)`: Returns k largest elements.
- `heapq.nsmallest(k, iterable, key)`: Returns k smallest elements.
- Python's heap is a **min heap** (smallest element at the top).

### `Counter`
- A dictionary subclass for counting.
- `Counter([1,1,2])` → `Counter({1: 2, 2: 1})`
- `.keys()` returns the unique elements.
- `.values()` returns the counts.
- `.most_common(k)` returns the k most common elements as (element, count) tuples.

### `lambda`
- Creates a small anonymous (unnamed) function.
- `lambda x: freq[x]` is a function that takes `x` and returns `freq[x]`.
- Equivalent to:
  ```python
  def get_freq(x):
      return freq[x]
  ```

### `map(function, iterable)`
- Applies a function to every element of an iterable.
- `map(int, ["1", "2", "3"])` → converts each string to int.
- Returns a map object (lazy evaluation). Use `list()` to get a list.

---

## G. Why This Method and Not Another Method?

### Why Counter + nlargest?
- `Counter` handles frequency counting in O(n).
- `nlargest` handles top-k selection in O(n log k) (or O(d log k) where d = distinct elements).
- Clean, readable, and efficient.

### Alternative 1: Sorting
- Count frequencies, then sort by frequency.
- Time: O(n + d log d) where d = number of distinct elements.
- If d is close to n, this is O(n log n) — worse than O(n log k) when k is small.
- **Acceptable** but not optimal.

### Alternative 2: Bucket Sort (O(n))
- Create buckets where index = frequency, value = list of elements with that frequency.
- Walk from the highest frequency bucket down, collecting k elements.
- Time: O(n) — the fastest approach.
- **This achieves O(n) mentioned in the PDF** but is slightly more complex to implement.

### Alternative 3: Manual Min Heap
- Build a min heap of size k manually using `heappush` and `heappop`.
- Same O(n log k) time as `nlargest`, but more code.
- **Not needed** when `nlargest` does the same thing.

### Advantages of Our Approach:
- Concise code using Python's standard library.
- O(n log k) time — efficient for small k.
- Easy to understand and explain.

---

## H. Time and Space Complexity

### Time Complexity: O(n log k)
- Counting: O(n) using Counter.
- Finding top k: O(d log k) where d = distinct elements ≤ n.
- Total: O(n + d log k) = O(n log k).

### Space Complexity: O(n)
- `Counter` stores up to n entries (if all elements are unique).
- The result list has k elements.
- Total: O(n).

### Why O(n log k) and not O(n log n)?
- We only maintain a heap of size k, not n.
- Each heap operation on a size-k heap takes O(log k), not O(log n).
- Since k ≤ n, O(log k) ≤ O(log n).

---

## I. Faculty Viva Questions and Answers

### Q1: What is a heap?
**A:** A heap is a complete binary tree where each parent is smaller (min heap) or larger (max heap) than its children. It provides O(log n) insertion and O(1) access to the minimum (or maximum) element.

### Q2: Why use a min heap of size k instead of a max heap?
**A:** A min heap of size k lets us efficiently maintain the top k elements. When we encounter a new element, we compare it with the minimum of the heap. If it's larger, we replace the minimum. This way, after processing all elements, the heap contains exactly the k largest.

### Q3: What is Counter in Python?
**A:** `Counter` is a class from the `collections` module that counts how many times each element appears. It's like a dictionary where keys are elements and values are their counts.

### Q4: What is a lambda function?
**A:** A lambda is a small, anonymous function defined in one line. `lambda x: freq[x]` takes input `x` and returns `freq[x]`. It's used here as the comparison key for `nlargest`.

### Q5: Could you use Counter.most_common(k) instead?
**A:** Yes! `Counter.most_common(k)` returns the k most common elements as (element, count) tuples. It uses a similar heap internally. Our approach using `nlargest` is equivalent.

### Q6: What is the bucket sort approach for this problem?
**A:** Create an array of size n+1 where index i holds all elements with frequency i. Then iterate from the end to collect k elements. This is O(n) time but uses O(n) extra space for the buckets.

### Q7: What happens if k equals the number of distinct elements?
**A:** All distinct elements are returned. The output includes every unique number in the array, ordered by frequency.

### Q8: What does `map(int, input().split())` do?
**A:** It reads a line of space-separated values, splits them into a list of strings, then converts each string to an integer. For example, `"1 2 3"` becomes `[1, 2, 3]`.

### Q9: What is the difference between `heapq.nlargest` and sorting?
**A:** `nlargest(k, ...)` is O(n log k) while sorting is O(n log n). When k is much smaller than n, `nlargest` is faster because it only maintains a small heap.

### Q10: What if two elements have the same frequency?
**A:** The problem says "any order is accepted" for ties. Our solution outputs them in the order `nlargest` returns, which is fine.

### Q11: What real-world applications use top-k frequent elements?
**A:** Trending topics on social media, most popular search queries, recommendation systems, network traffic analysis, and natural language processing (most common words).

### Q12: Can this be solved with a single for loop?
**A:** The counting part can be done in a single loop, but finding the top k still requires either sorting, a heap, or bucket sort. You cannot find top k in a single pass through unsorted data without additional processing.

---

## J. VS Code Execution

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q5_Top_K_Frequent.py
6 2
1 1 1 2 2 3
1 2
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q5_Top_K_Frequent.py
9 3
4 4 1 1 1 2 2 2 2
2 1 4
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | Hash Map counting + Heap-based top-k selection |
| **Data Structure** | Counter (hash map) + Min Heap (via nlargest) |
| **Core Logic** | 1. Count frequencies with Counter. 2. Use heapq.nlargest to get k most frequent. 3. Print results. |
| **Memory Trick** | "Count with Counter, pick with nlargest" |
| **One Sentence** | Count element frequencies using Counter, then extract the k elements with the highest frequencies using heapq.nlargest. |
