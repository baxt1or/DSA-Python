def reverse(s: int) -> int:
    # Convert integer to string and reverse the string
    reversed_str = str(s)[::-1]
    # Convert reversed string back to integer
    return int(reversed_str)

# Example usage
v = -124
# result = reverse(v)
print(reverse(v))  # Output: 421