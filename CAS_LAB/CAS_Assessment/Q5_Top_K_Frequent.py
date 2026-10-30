# Q5: Top K Frequent Elements
# Algorithm: Hash Map + Min Heap
# Time Complexity: O(n log k) | Space Complexity: O(n)

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Find the k most frequent elements in the array.
    Uses a hash map to count frequencies, then a min heap of size k
    to extract the top k frequent elements.
    """
    # Step 1: Count the frequency of each element
    freq = Counter(nums)
    
    # Step 2: Use a min heap of size k to find top k elements
    # heapq.nlargest returns the k largest items based on the key
    # We use frequency as the key
    top_k = heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])
    
    return top_k


# ---- Main Program ----
# Read n and k from the first line
first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])

# Read the array of integers
nums = list(map(int, input().split()))

# Find and print the top k frequent elements
result = top_k_frequent(nums, k)
print(' '.join(map(str, result)))
