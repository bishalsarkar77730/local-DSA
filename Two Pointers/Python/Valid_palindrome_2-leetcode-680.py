s = "aba"

def is_palindrome_range(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            skip_left = is_palindrome_range(s, left + 1, right)
            skip_right = is_palindrome_range(s, left, right - 1)
            return skip_left or skip_right
    return True
