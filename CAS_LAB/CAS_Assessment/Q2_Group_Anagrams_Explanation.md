# Q2: Group Anagrams — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Given a list of strings, group together all strings that are **anagrams** of each other.

### What is an anagram?
Two strings are anagrams if you can rearrange the letters of one to form the other. They have the **same characters with the same frequencies**, just in different order.
- "eat" and "tea" are anagrams (both have: a, e, t).
- "tan" and "nat" are anagrams (both have: a, n, t).
- "bat" is not an anagram of "eat" (different characters).

### What input do we receive?
- First line: an integer `n` (number of strings).
- Next `n` lines: one lowercase string per line.

### What output do we produce?
- Print each group of anagrams on a separate line, with words separated by spaces.

### Small Example
```
Input: eat, tea, tan, ate, nat, bat
Groups: [eat, tea, ate], [tan, nat], [bat]
Output:
eat tea ate
tan nat
bat
```

---

## B. Algorithm and Approach

### Approach: Hashing with Sorted Key

The key insight is: **if you sort the characters of two anagrams, you get the same string**.
- `sorted("eat")` → `['a', 'e', 't']` → `"aet"`
- `sorted("tea")` → `['a', 'e', 't']` → `"aet"`
- `sorted("ate")` → `['a', 'e', 't']` → `"aet"`

So we can use the sorted version as a **dictionary key** and group all words that share the same key.

### Step-by-Step Logic:
1. Create an empty dictionary where key = sorted string, value = list of original words.
2. For each word in the input:
   - Sort its characters to get the key.
   - Add the original word to the list at that key.
3. Print each group (each list in the dictionary).

### Why this approach?
- Sorting each string of length k takes O(k log k).
- For n strings with average length k, total time is O(n × k log k).
- The PDF expects O(n × k). We can achieve exactly O(n × k) using character counting (see alternatives below), but the sorted approach is simpler and close enough for practical purposes.
- Using character count as key achieves true O(n × k) since counting k characters is O(k).

---

## C. Complete Python Code

```python
from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_key = ''.join(sorted(word))
        anagram_groups[sorted_key].append(word)
    return anagram_groups

n = int(input())
words = []
for i in range(n):
    words.append(input().strip())

groups = group_anagrams(words)

for key in groups:
    print(' '.join(groups[key]))
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
6
eat
tea
tan
ate
nat
bat
```
**Expected Output:**
```
eat tea ate
tan nat
bat
```
**Explanation:**
- "eat" sorts to "aet" → group: [eat]
- "tea" sorts to "aet" → group: [eat, tea]
- "tan" sorts to "ant" → group: [tan]
- "ate" sorts to "aet" → group: [eat, tea, ate]
- "nat" sorts to "ant" → group: [tan, nat]
- "bat" sorts to "abt" → group: [bat]
- Final groups: `eat tea ate`, `tan nat`, `bat`

### Test Case 2
**Input:**
```
4
listen
silent
enlist
google
```
**Expected Output:**
```
listen silent enlist
google
```
**Explanation:**
- "listen" sorts to "eilnst"
- "silent" sorts to "eilnst" → same group
- "enlist" sorts to "eilnst" → same group
- "google" sorts to "eggloo" → different group
- Final groups: `listen silent enlist`, `google`

---

## E. Detailed Code Explanation

### Line: `from collections import defaultdict`
- Imports `defaultdict` from Python's `collections` module.
- A `defaultdict(list)` automatically creates an empty list as the default value for new keys.
- Without this, we would need to check `if key not in dict` before appending.

### Line: `anagram_groups = defaultdict(list)`
- Creates a dictionary where every new key automatically gets an empty list `[]`.
- Example: `anagram_groups["aet"]` returns `[]` the first time, then we can append to it.

### Line: `sorted_key = ''.join(sorted(word))`
- `sorted(word)` returns a list of characters in alphabetical order. Example: `sorted("eat")` → `['a', 'e', 't']`
- `''.join(...)` joins the list back into a string: `"aet"`
- This string serves as a unique identifier for the anagram group.

### Line: `anagram_groups[sorted_key].append(word)`
- Adds the original word to the list at the sorted key.
- All anagrams of the same word will share the same sorted key.

### Line: `print(' '.join(groups[key]))`
- Joins the words in each group with spaces and prints them on one line.

---

## F. Python Syntax Explanation

### `from ... import ...`
- Imports a specific item from a module.
- `from collections import defaultdict` brings in only `defaultdict`, not the entire `collections` module.

### `defaultdict(list)`
- A special dictionary from `collections`.
- When you access a key that doesn't exist, instead of raising `KeyError`, it creates a default value.
- `defaultdict(list)` uses an empty list `[]` as the default.
- `defaultdict(int)` would use `0` as the default.

### `sorted()`
- Returns a new sorted list from the given iterable.
- Does NOT modify the original. `sorted("tea")` → `['a', 'e', 't']`

### `''.join()`
- Joins elements of a list into a single string.
- `''.join(['a', 'e', 't'])` → `"aet"`
- The string before `.join()` is the separator. `' '.join(["eat", "tea"])` → `"eat tea"`

### `strip()`
- Removes leading and trailing whitespace from a string.
- Used here to clean up any trailing newline characters from input.

### `append()`
- Adds an element to the end of a list.
- `words.append("eat")` adds `"eat"` to the `words` list.

---

## G. Why This Method and Not Another Method?

### Why Sorted Key Hashing?
- Simple and easy to understand.
- Sorting characters makes all anagrams produce the same key.
- Dictionary grouping is natural and efficient.

### Alternative 1: Character Count as Key (True O(n × k))
- Instead of sorting, count the frequency of each character (26 lowercase letters).
- Use the count tuple as the dictionary key.
- Example: "eat" → (1,0,0,0,1,0,...,1,...,0) — counts of a=1, e=1, t=1
- Time: O(n × k) — counting k characters is O(k), no sorting needed.
- **This is actually the optimal approach per the PDF**, but it's harder to explain and debug.
- Our sorted approach is O(n × k log k), which is very close and much simpler.

### Alternative 2: Compare Every Pair
- Compare each string with every other string to check if they are anagrams.
- Time: O(n² × k) — too slow for n up to 10,000.
- **Rejected** due to poor performance.

### Advantages of Our Approach:
- Clean, readable code.
- Easy to explain in a viva.
- `defaultdict` simplifies the grouping logic.
- Close to optimal time complexity.

### If constraints increased?
- For very large k, the character count approach would be faster (O(k) vs O(k log k) per word).
- For very large n, the overall approach remains the same — just more groups in the dictionary.

---

## H. Time and Space Complexity

### Time Complexity: O(n × k log k)
- `n` = number of strings.
- `k` = average length of each string.
- Sorting each string takes O(k log k).
- We sort n strings, so total: O(n × k log k).
- Dictionary operations (insert, lookup) are O(k) for each key (because keys are strings of length k that need hashing).
- The PDF expects O(n × k), achievable with character counting, but our approach is close.

### Space Complexity: O(n × k)
- We store all n strings in the dictionary.
- Each string has average length k.
- Total space: O(n × k).

---

## I. Faculty Viva Questions and Answers

### Q1: What is an anagram?
**A:** An anagram is a word formed by rearranging the letters of another word. For example, "listen" and "silent" are anagrams — they have the same letters in different order.

### Q2: Why did you sort the characters?
**A:** Sorting makes all anagrams produce the same string. For example, "eat", "tea", and "ate" all sort to "aet". This gives us a consistent key for grouping.

### Q3: What is a defaultdict?
**A:** A `defaultdict` is a special dictionary that automatically creates a default value when you access a key that doesn't exist. `defaultdict(list)` creates an empty list for new keys, so we can directly append without checking if the key exists.

### Q4: How would you achieve true O(n × k) complexity?
**A:** Instead of sorting, count the frequency of each of the 26 letters and use the resulting tuple as the key. Counting takes O(k) per word instead of O(k log k) for sorting.

### Q5: What if the strings could contain uppercase letters?
**A:** We would convert all strings to lowercase first using `.lower()`, or we would handle uppercase and lowercase as separate characters depending on the problem requirements.

### Q6: Does the order of groups matter?
**A:** No, the problem states "Group and element ordering are not significant." So any order of groups and any order within groups is acceptable.

### Q7: What is the time complexity of dictionary lookup in Python?
**A:** O(1) on average. Python dictionaries use hash tables internally, which provide constant-time average lookup.

### Q8: Why not use a regular dictionary instead of defaultdict?
**A:** We could, but we would need to write extra code to check if the key exists before appending. With `defaultdict(list)`, we can directly do `dict[key].append(word)` without any check. It makes the code cleaner.

### Q9: Can two different (non-anagram) words produce the same sorted key?
**A:** No. If two words have the same sorted characters, they must be anagrams by definition — same characters, same frequencies.

### Q10: What is the difference between `sorted()` and `.sort()`?
**A:** `sorted()` returns a new sorted list and does not modify the original. `.sort()` modifies the list in-place and returns `None`. We use `sorted()` because strings are immutable in Python — we cannot sort a string in-place.

### Q11: What happens if all strings are anagrams of each other?
**A:** All strings will have the same sorted key, so they will all be in one group. The dictionary will have only one entry.

### Q12: What real-world application uses grouping by anagrams?
**A:** Word games (like Scrabble), spell checkers, cryptography (substitution ciphers), and search engines that suggest alternative word arrangements.

---

## J. VS Code Execution

### Step-by-Step:
1. Open VS Code.
2. Open the `CAS_Assessment` folder.
3. Open `Q2_Group_Anagrams.py`.
4. Open the terminal: `Terminal → New Terminal` or `` Ctrl+` ``.
5. Run: `python Q2_Group_Anagrams.py`
6. Enter the input line by line and press Enter after each line.

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q2_Group_Anagrams.py
6
eat
tea
tan
ate
nat
bat
eat tea ate
tan nat
bat
```

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q2_Group_Anagrams.py
4
listen
silent
enlist
google
listen silent enlist
google
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Algorithm** | Hashing with Sorted Key |
| **Data Structure** | Dictionary (defaultdict with lists) |
| **Core Logic** | 1. Sort each word's characters to get a key. 2. Group words with the same key. 3. Print each group. |
| **Memory Trick** | "Sort to match, dict to group" |
| **One Sentence** | Sort each word's characters to create a common key, then use a dictionary to group all anagrams together. |
