# Q2: Group Anagrams
# Algorithm: Hashing with sorted key
# Time Complexity: O(n * k) where k is average string length | Space: O(n * k)

from collections import defaultdict

def group_anagrams(words):
    """
    Group strings that are anagrams of each other.
    Two strings are anagrams if they contain the same characters
    in the same frequency, just in different order.
    """
    # Dictionary where key = sorted characters, value = list of anagrams
    anagram_groups = defaultdict(list)
    
    for word in words:
        # Sort the characters of the word to create a unique key
        # All anagrams will produce the same sorted key
        # Example: "eat" -> "aet", "tea" -> "aet", "ate" -> "aet"
        sorted_key = ''.join(sorted(word))
        
        # Add the original word to the group with this key
        anagram_groups[sorted_key].append(word)
    
    return anagram_groups


# ---- Main Program ----
# Read number of strings
n = int(input())

# Read each string
words = []
for i in range(n):
    words.append(input().strip())

# Group the anagrams
groups = group_anagrams(words)

# Print each group on a separate line, words separated by spaces
for key in groups:
    print(' '.join(groups[key]))
