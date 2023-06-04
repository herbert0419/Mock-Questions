def firstUniqChar(s):
    """
    Find the first non-repeating character in the string and return its index.
    If it does not exist, return -1.
    """
    # Create a frequency dictionary to count the occurrences of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Traverse the string to find the first non-repeating character
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    # If no non-repeating character is found, return -1
    return -1

s = "leetcode"
result = firstUniqChar(s)
print(result)  # Output: 0


s = "aabb"
result = firstUniqChar(s)
print(result)  # Output: -1


s = "loveleetcode"
result = firstUniqChar(s)
print(result)  # Output: 2

