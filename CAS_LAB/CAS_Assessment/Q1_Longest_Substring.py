# Q1: Longest Substring Without Repeating Characters
# Algorithm: Sliding Window with Hash Set
# Time Complexity: O(n) | Space Complexity: O(min(n, m)) where m is character set size

def longest_substring_without_repeating(s):
    """
    Find the length of the longest substring without repeating characters.
    Uses a sliding window approach with two pointers and a dictionary.
    """
    # Dictionary to store the last seen index of each character
    char_index = {}
    
    # Left pointer of the sliding window
    left = 0
    
    # Variable to track the maximum length found
    max_length = 0
    
    # Right pointer moves through the string one character at a time
    for right in range(len(s)):
        current_char = s[right]
        
        # If we have seen this character before AND it is within our current window
        if current_char in char_index and char_index[current_char] >= left:
            # Move the left pointer to one position after the last occurrence
            left = char_index[current_char] + 1
        
        # Update the last seen index of the current character
        char_index[current_char] = right
        
        # Calculate the current window length and update max_length
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length


# ---- Main Program ----
# Read input string
s = input()

# Call the function and print the result
print(longest_substring_without_repeating(s))
