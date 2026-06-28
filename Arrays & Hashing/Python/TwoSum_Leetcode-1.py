# given = [
#     nums = [2,7,11,15],
#     target = 9,
#     output = should be in index [0,1]
# ]

# Conditions = [
#     the 9 should be derived by the sum of two numbers only
#     if list is empty
# ]

nums = [2, 7, 11, 15]
target = 9


def twosum():
    length = len(nums)
    if length <= 0:
        print("List is Empty")
        return
    else:
        for num in range(length):
            for i in range(num + 1, length):
                if nums[num] + nums[i] == target:
                    print([num, i])
                    return


twosum()
