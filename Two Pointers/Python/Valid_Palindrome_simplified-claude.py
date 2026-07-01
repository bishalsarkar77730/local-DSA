# Given a string s, return true if it reads the same forwards and backwards.
# Examples :- "racecar" → true, "hello" → false, "a" → true


# Dont do this on Interview
# s = "hello"
# l = s[::-1]
# if s == l:
#     print("true")
# else:
#     print("false")


s = "racecar"


def is_palindrom():
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            print("false")
            return False
        left += 1
        right -= 1
    print("true")
    return True

is_palindrom()
