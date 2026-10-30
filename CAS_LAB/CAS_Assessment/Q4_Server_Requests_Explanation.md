# Q4: Analyze Server Requests — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
We are given server logs. Each log entry contains an **IP address** and an **HTTP status code**. We need to find:
1. The **most active IP** (the IP that appears the most). If there's a tie, pick the **lexicographically smallest** IP.
2. The **total number of 4xx responses** (status codes 400–499).
3. The **total number of 5xx responses** (status codes 500–599).

### What are HTTP status codes?
- **2xx (200–299)**: Success (e.g., 200 OK)
- **4xx (400–499)**: Client errors (e.g., 404 Not Found)
- **5xx (500–599)**: Server errors (e.g., 500 Internal Server Error)

### What input do we receive?
- First line: `n` (number of log entries).
- Next `n` lines: `IP_ADDRESS STATUS_CODE` separated by a space.

### What output do we produce?
Three lines:
1. Most active IP address.
2. Count of 4xx responses.
3. Count of 5xx responses.

### Small Example
```
Logs: 192.168.1.10 200, 192.168.1.11 404, 192.168.1.10 500
- IP 192.168.1.10 appears 2 times (most active)
- 4xx count: 1 (the 404)
- 5xx count: 1 (the 500)
```

---

## B. Algorithm and Approach

### Approach: Single Pass with Dictionary

1. Read all log entries in one pass.
2. Use a dictionary to count how many times each IP appears.
3. Keep separate counters for 4xx and 5xx responses.
4. After processing all logs, find the IP with the highest count (break ties lexicographically).

### Why Single Pass?
- We process each log entry exactly once — O(n) time.
- Dictionary operations (insert, update, lookup) are O(1).
- Finding the most active IP requires one more pass through the dictionary — O(k) where k is unique IPs.
- Total: O(n + k) = O(n) since k ≤ n.

### What does "lexicographically smallest" mean?
It means alphabetical order for strings. For IP addresses:
- Compare character by character.
- "10.0.0.1" < "10.0.0.2" < "192.168.1.10"
- Python's `<` operator on strings does lexicographic comparison by default.

---

## C. Complete Python Code

```python
def analyze_server_requests():
    n = int(input())
    ip_count = {}
    count_4xx = 0
    count_5xx = 0

    for i in range(n):
        parts = input().split()
        ip_address = parts[0]
        status_code = int(parts[1])
        
        if ip_address in ip_count:
            ip_count[ip_address] += 1
        else:
            ip_count[ip_address] = 1
        
        if 400 <= status_code <= 499:
            count_4xx += 1
        elif 500 <= status_code <= 599:
            count_5xx += 1

    most_active_ip = None
    max_requests = 0
    for ip in ip_count:
        requests = ip_count[ip]
        if requests > max_requests:
            max_requests = requests
            most_active_ip = ip
        elif requests == max_requests:
            if ip < most_active_ip:
                most_active_ip = ip

    print(most_active_ip)
    print(count_4xx)
    print(count_5xx)

analyze_server_requests()
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
6
192.168.1.10 200
192.168.1.11 404
192.168.1.10 500
192.168.1.12 404
192.168.1.11 200
192.168.1.10 200
```
**Expected Output:**
```
192.168.1.10
2
1
```
**Explanation:**
- IP counts: `192.168.1.10` → 3, `192.168.1.11` → 2, `192.168.1.12` → 1
- Most active: `192.168.1.10` (3 requests)
- 4xx responses: 404 (line 2) + 404 (line 4) = **2**
- 5xx responses: 500 (line 3) = **1**

### Test Case 2
**Input:**
```
5
10.0.0.2 404
10.0.0.1 404
10.0.0.2 200
10.0.0.1 200
10.0.0.3 503
```
**Expected Output:**
```
10.0.0.1
2
1
```
**Explanation:**
- IP counts: `10.0.0.2` → 2, `10.0.0.1` → 2, `10.0.0.3` → 1
- Tie between `10.0.0.1` and `10.0.0.2` (both have 2 requests).
- Lexicographically: `"10.0.0.1" < "10.0.0.2"`, so most active = `10.0.0.1`
- 4xx: 404 + 404 = **2**
- 5xx: 503 = **1**

---

## E. Detailed Code Explanation

### Line: `ip_count = {}`
- An empty dictionary to store how many requests each IP has made.
- Key: IP address (string), Value: count (integer).

### Line: `count_4xx = 0` and `count_5xx = 0`
- Counters for 4xx and 5xx response codes.
- Initialized to zero before processing starts.

### Line: `parts = input().split()`
- Reads a line like `"192.168.1.10 200"` and splits it into `["192.168.1.10", "200"]`.
- `parts[0]` = IP address, `parts[1]` = status code.

### Line: `status_code = int(parts[1])`
- Converts the status code from string to integer for numerical comparison.

### Lines: Counting IPs
```python
if ip_address in ip_count:
    ip_count[ip_address] += 1
else:
    ip_count[ip_address] = 1
```
- If the IP already exists in the dictionary, increment its count.
- If it's a new IP, initialize its count to 1.

### Lines: Counting 4xx and 5xx
```python
if 400 <= status_code <= 499:
    count_4xx += 1
elif 500 <= status_code <= 599:
    count_5xx += 1
```
- Python supports chained comparison: `400 <= status_code <= 499` means `400 <= status_code AND status_code <= 499`.
- `elif` (else if) ensures we only check 5xx if it's not 4xx.

### Lines: Finding Most Active IP
```python
if requests > max_requests:
    max_requests = requests
    most_active_ip = ip
elif requests == max_requests:
    if ip < most_active_ip:
        most_active_ip = ip
```
- First `if`: Update if this IP has strictly more requests.
- `elif`: On a tie, update only if this IP is lexicographically smaller.
- Python's `<` on strings does lexicographic comparison.

---

## F. Python Syntax Explanation

### Chained Comparison
- `400 <= status_code <= 499` is equivalent to `status_code >= 400 and status_code <= 499`.
- This is a Python-specific feature not available in many other languages.

### Dictionary Operations
- `ip_count[ip] += 1`: Increment the value at key `ip`.
- `ip in ip_count`: Check if key exists.
- `for ip in ip_count`: Iterate through all keys.

### `input().split()`
- `input()` reads a line as a string.
- `.split()` splits by whitespace and returns a list of strings.

### `int()`
- Converts a string to an integer.
- `int("404")` → `404`

### String Comparison with `<`
- Python compares strings character by character using Unicode values.
- `"10.0.0.1" < "10.0.0.2"` → `True` (because '1' < '2' at the 7th position).

---

## G. Why This Method and Not Another Method?

### Why Dictionary Counting?
- Simple, direct approach.
- O(1) per insertion and lookup.
- O(n) total time — meets the expected complexity.

### Alternative 1: Sorting
- Sort the log entries by IP, then count consecutive same IPs.
- Time: O(n log n) — worse than O(n).
- **Rejected** because it doesn't meet the expected time complexity.

### Alternative 2: collections.Counter
- `Counter` is a specialized dictionary for counting.
- Could simplify the counting code.
- However, using a plain dictionary is more transparent and easier to explain.
- Both have the same O(n) performance.

### Alternative 3: Pandas DataFrame
- Overkill for this problem.
- Requires an external library.
- Not standard in a coding assessment.
- **Rejected**.

### Advantages of Our Approach:
- O(n) time — optimal.
- O(k) space — only stores unique IPs.
- Simple, readable code.
- No external libraries needed.

---

## H. Time and Space Complexity

### Time Complexity: O(n)
- Processing each log entry: O(1) per entry × n entries = O(n).
- Finding the most active IP: O(k) where k = unique IPs ≤ n.
- Total: O(n + k) = O(n).

### Space Complexity: O(k)
- `k` = number of unique IP addresses.
- The dictionary `ip_count` stores one entry per unique IP.
- In the worst case (all unique IPs), k = n, so space is O(n).

---

## I. Faculty Viva Questions and Answers

### Q1: What are HTTP status codes?
**A:** HTTP status codes are three-digit numbers returned by a web server to indicate the result of a request. 2xx means success, 3xx means redirection, 4xx means client error, and 5xx means server error.

### Q2: What is a 404 error?
**A:** 404 means "Not Found." The server could not find the requested resource. For example, accessing a webpage that doesn't exist.

### Q3: What does "lexicographically smallest" mean?
**A:** It means the first in alphabetical/dictionary order. For strings, Python compares character by character. For IP addresses like "10.0.0.1" and "10.0.0.2", the first is lexicographically smaller.

### Q4: Why did you use a dictionary instead of a list?
**A:** A dictionary provides O(1) lookup by key (IP address). With a list, we would need to search through all entries to find an IP, which is O(n). The dictionary is much more efficient.

### Q5: Could you use Counter from collections?
**A:** Yes, `Counter(ip_list).most_common(1)` would give the most frequent IP. But it doesn't handle the tie-breaking rule (lexicographically smallest). I used a manual dictionary to handle ties properly.

### Q6: What happens if all status codes are 200?
**A:** Both `count_4xx` and `count_5xx` would be 0. The most active IP would still be correctly identified based on frequency.

### Q7: How does Python compare IP addresses as strings?
**A:** Character by character. "10.0.0.1" vs "192.168.1.1": '1' == '1', then '0' < '9', so "10.0.0.1" is smaller. Note: this is lexicographic, not numerical comparison of IP octets.

### Q8: What is the difference between `if-elif-else` and multiple `if` statements?
**A:** `if-elif-else` is a chain where only one branch executes. Multiple `if` statements are independent — each one is checked. Here, we use `elif` because a status code can only be 4xx or 5xx, not both.

### Q9: What would happen with 10^6 log entries?
**A:** Our O(n) algorithm handles it efficiently. Processing 1 million entries takes a second or less on modern hardware.

### Q10: What is O(k) space?
**A:** `k` is the number of unique IP addresses. We store exactly one dictionary entry per unique IP. If there are 100 unique IPs among 1 million logs, we only use space for 100 entries.

### Q11: Can this solution handle IPv6 addresses?
**A:** Yes, because we treat IP addresses as strings. The algorithm doesn't parse or interpret the IP format — it just counts and compares strings.

### Q12: What data structure does Python use internally for dictionaries?
**A:** Python dictionaries use **hash tables** with open addressing. They provide O(1) average-case lookup, insertion, and deletion.

---

## J. VS Code Execution

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q4_Server_Requests.py
6
192.168.1.10 200
192.168.1.11 404
192.168.1.10 500
192.168.1.12 404
192.168.1.11 200
192.168.1.10 200
192.168.1.10
2
1
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q4_Server_Requests.py
5
10.0.0.2 404
10.0.0.1 404
10.0.0.2 200
10.0.0.1 200
10.0.0.3 503
10.0.0.1
2
1
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | Single-pass counting with dictionary |
| **Data Structure** | Dictionary for IP counting, integer counters for 4xx/5xx |
| **Core Logic** | 1. Count each IP in a dictionary. 2. Count 4xx and 5xx separately. 3. Find IP with max count (break ties lexicographically). |
| **Memory Trick** | "Count IPs in dict, count errors by range, pick max with min string" |
| **One Sentence** | Use a dictionary to count IP frequencies and integer counters for error codes, then find the most active IP with lexicographic tie-breaking. |
