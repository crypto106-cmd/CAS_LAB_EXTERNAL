# Q1: Longest Substring Without Repeating Characters — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
We are given a string `s`. We need to find the **longest substring** (a continuous portion of the string) where **no character repeats**. We return the **length** of that substring.

### What is a substring?
A substring is a contiguous sequence of characters within a string. For example, in `"abcab"`, the substrings include `"a"`, `"ab"`, `"abc"`, `"bca"`, `"cab"`, etc.

### What input do we receive?
- A single string `s` which may contain letters, digits, symbols, and spaces.

### What output do we produce?
- A single integer — the length of the longest substring with all unique characters.

### Small Example
```
Input:  abcabcbb
```
- Substring "abc" has length 3 (all unique).
- Substring "bca" has length 3 (all unique).
- Substring "abcab" has length 5 but has repeating 'a' and 'b' — NOT valid.
- So the answer is **3**.

---

## B. Algorithm and Approach

### Approach: Sliding Window with Two Pointers

Imagine a window over the string. The window has a **left boundary** and a **right boundary**. We expand the window to the right, character by character. If we encounter a character that already exists in the window, we shrink the window from the left until the duplicate is removed.

### Step-by-Step Logic:
1. Start with both `left` and `right` pointers at position 0.
2. Use a dictionary to remember the **last index** where each character was seen.
3. Move `right` pointer one step at a time through the string.
4. For each character at `right`:
   - If we have seen this character before and its last position is **within** our current window (`>= left`), move `left` to one position after the previous occurrence.
   - Update the character's last seen position to `right`.
   - Calculate the window size (`right - left + 1`) and update the maximum.
5. After processing all characters, return the maximum length found.

### Why Sliding Window?
- A brute force approach would check every possible substring — that's O(n²) or O(n³).
- The sliding window visits each character at most twice (once by `right`, once by `left`), giving us **O(n) time**.

---

## C. Complete Python Code

```python
def longest_substring_without_repeating(s):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        current_char = s[right]
        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1
        char_index[current_char] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length

s = input()
print(longest_substring_without_repeating(s))
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
abcabcbb
```
**Expected Output:**
```
3
```
**Explanation:**
- Window expands: `a` → `ab` → `abc` (length 3).
- At index 3, `a` is repeated. Window becomes `bca` (left moves to 1). Length is still 3.
- At index 4, `b` is repeated. Window becomes `cab` (left moves to 2). Length is still 3.
- At index 5, `c` is repeated. Window becomes `abc` (left moves to 3). Wait — actually it becomes `b` → then `bc` → `bcb`... the window shrinks. The max never exceeds 3.
- **Answer: 3**

### Test Case 2
**Input:**
```
bbbbb
```
**Expected Output:**
```
1
```
**Explanation:**
- Every character is `b`.
- Each time `right` moves, `b` is already in the window, so `left` jumps to `right`.
- The window size is always 1.
- **Answer: 1**

---

## E. Detailed Code Explanation

### Line: `char_index = {}`
- Creates an empty **dictionary**.
- Purpose: Store the most recent index at which each character was seen.
- Without this, we would not know where duplicates are.

### Line: `left = 0`
- Initializes the left boundary of our sliding window.
- The window starts from the beginning of the string.

### Line: `max_length = 0`
- Keeps track of the longest valid substring length found so far.
- Starts at 0 because we haven't processed any character yet.

### Line: `for right in range(len(s)):`
- `right` is the right boundary of our window.
- It moves from index 0 to the last index of the string.
- Each iteration processes one new character.

### Line: `current_char = s[right]`
- Gets the character at the current right position.
- Stored in a variable for cleaner code.

### Line: `if current_char in char_index and char_index[current_char] >= left:`
- **First condition**: Checks if we have seen this character before.
- **Second condition**: Checks if the previous occurrence is within our current window (at or after `left`).
- Both conditions must be true for us to shrink the window.
- If the previous occurrence is before `left`, it's already outside our window, so it doesn't matter.

### Line: `left = char_index[current_char] + 1`
- Moves `left` to one position after the duplicate character.
- This ensures the duplicate is no longer inside the window.

### Line: `char_index[current_char] = right`
- Updates the dictionary with the new position of the current character.
- This is done regardless of whether we found a duplicate.

### Lines: `current_length = right - left + 1` and `if current_length > max_length:`
- Calculates the size of the current valid window.
- Updates the maximum if the current window is larger.

### Line: `return max_length`
- Returns the final answer — the maximum length found.

---

## F. Python Syntax Explanation

### `def` and `return`
- `def` defines a function. `def longest_substring_without_repeating(s):` creates a function that takes a string `s` as input.
- `return max_length` sends the result back to wherever the function was called.

### Dictionary `{}`
- A dictionary stores key-value pairs. Here, the key is a character and the value is its last seen index.
- `char_index[current_char]` accesses the value for the given character.
- `current_char in char_index` checks if the character exists as a key.

### `for` loop with `range()`
- `range(len(s))` generates numbers from 0 to `len(s) - 1`.
- The `for` loop iterates through each number, which we use as an index.

### `input()`
- Reads one line of text from the terminal.
- Returns a string.

### `print()`
- Prints the value to the terminal.

### `and` (logical operator)
- Both conditions on either side must be `True` for the overall expression to be `True`.

---

## G. Why This Method and Not Another Method?

### Why Sliding Window?
- It gives us **O(n) time** — the best possible for this problem since we must read every character at least once.
- It uses only a dictionary for storage — **O(min(n, m)) space** where m is the character set size.

### Alternative 1: Brute Force (Check All Substrings)
- Generate every possible substring and check if all characters are unique.
- Time: O(n³) — way too slow for n up to 50,000.
- **Rejected** because of poor performance.

### Alternative 2: Brute Force with Set
- For each starting position, expand and use a set to detect duplicates.
- Time: O(n²) — still too slow.
- **Rejected** because it doesn't meet the expected O(n) complexity.

### Alternative 3: Sliding Window with Set (instead of Dictionary)
- Instead of a dictionary, use a set and remove characters from the left one by one when a duplicate is found.
- Time: Still O(n) because each character is added and removed at most once.
- Works correctly but slightly less efficient because we may need to remove multiple characters from the left.
- Our dictionary approach jumps `left` directly to the right position.

### Advantages of Our Approach
- O(n) time — optimal.
- Simple and readable code.
- Dictionary lookup is O(1) on average.
- No need to delete characters from a set one by one.

### If constraints increased?
- If n could be 10^8 or more, the algorithm would still work in O(n). We might need to optimize constant factors, but the approach remains the same.

---

## H. Time and Space Complexity

### Time Complexity: O(n)
- `n` is the length of the string.
- The `right` pointer visits each character exactly once: that's n iterations.
- The `left` pointer only moves forward (never backward), so it also visits at most n positions total.
- Dictionary operations (lookup and update) are O(1) on average.
- Total: **O(n)**.

### Space Complexity: O(min(n, m))
- `m` is the size of the character set (e.g., 128 for ASCII, 26 for lowercase letters).
- The dictionary stores at most one entry per unique character.
- In the worst case (all unique characters), the dictionary has `min(n, m)` entries.

---

## I. Faculty Viva Questions and Answers

### Q1: What is a sliding window?
**A:** A sliding window is a technique where we maintain a range (window) over a sequence and slide it forward. Instead of recalculating everything from scratch, we update the window incrementally — adding new elements at the right and removing old elements from the left.

### Q2: Why did you use a dictionary instead of a set?
**A:** A dictionary stores the **index** of each character, allowing us to jump `left` directly to the correct position. A set only tells us whether a character exists, so we would need to remove characters one by one from the left until the duplicate is gone.

### Q3: What happens if the string is empty?
**A:** The `for` loop runs zero times (since `range(0)` is empty), and `max_length` stays at 0. The function returns 0, which is correct.

### Q4: What does `char_index[current_char] >= left` check?
**A:** It checks whether the previous occurrence of the character is inside our current window. If it's before `left`, it's already excluded from the window, so we don't need to shrink.

### Q5: Can this be solved using recursion?
**A:** Technically yes, but it would be inefficient and unnecessarily complex. The iterative sliding window approach is simpler, uses less memory (no recursion stack), and runs in O(n) time.

### Q6: What is the worst-case scenario for this algorithm?
**A:** When all characters are unique (e.g., `"abcdef..."`), the window keeps expanding without ever shrinking. The loop runs n times, so it's still O(n). When all characters are the same (e.g., `"aaaaa"`), the left pointer jumps forward every step, but total work is still O(n).

### Q7: What data structure is used internally by Python dictionaries?
**A:** Python dictionaries use **hash tables**. They provide O(1) average time for insertion, deletion, and lookup.

### Q8: Why not sort the string and find the longest unique run?
**A:** Sorting would destroy the order of characters. A substring must be contiguous in the original string, so sorting is not applicable here.

### Q9: What is the difference between a substring and a subsequence?
**A:** A **substring** is a contiguous portion of the string (e.g., "abc" in "xabcy"). A **subsequence** can skip characters but must maintain order (e.g., "ace" in "abcde"). This problem asks for a **substring**.

### Q10: Could you use two nested for loops instead?
**A:** Yes, that's the brute force approach. The outer loop picks the start, the inner loop expands the end. But it would be O(n²) which doesn't meet the expected O(n) time complexity.

### Q11: What happens if we remove the `char_index[current_char] >= left` check?
**A:** The algorithm would incorrectly move `left` backward to an old position that is already outside the window. This would give wrong answers because `left` should only move forward, never backward.

### Q12: Can this problem be solved using dynamic programming?
**A:** You could define dp[i] as the length of the longest valid substring ending at index i, but you would still need a way to find duplicates efficiently — essentially rebuilding the sliding window logic. The sliding window is the most natural approach.

---

## J. VS Code Execution

### Step-by-Step:
1. Open VS Code.
2. Open the `CAS_Assessment` folder.
3. Open `Q1_Longest_Substring.py`.
4. Open the terminal: `Terminal → New Terminal` or press `` Ctrl+` ``.
5. Run the program:
   ```
   python Q1_Longest_Substring.py
   ```
6. Enter the input and press Enter.

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q1_Longest_Substring.py
abcabcbb
3
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q1_Longest_Substring.py
bbbbb
1
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | Sliding Window with Two Pointers |
| **Data Structure** | Dictionary (hash map) |
| **Core Logic** | 1. Expand right pointer through the string. 2. If duplicate found within window, jump left pointer past it. 3. Track maximum window size. |
| **Memory Trick** | "Slide right, jump left on repeats, track max" |
| **One Sentence** | Use a sliding window with a dictionary to track character positions and find the longest substring where no character repeats. |
