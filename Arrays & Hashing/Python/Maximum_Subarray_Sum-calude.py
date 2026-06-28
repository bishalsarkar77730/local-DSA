# Given an array of integers nums, find the maximum (biggest) sum of any contiguous subarray (a subarray = consecutive elements). Return the sum.
# Example 1: nums = [1, 2, 3, -2, 5] → 9 (the whole array)
# Example 2: nums = [-3, -1, -2] → -1 (just the single element -1)
# Example 3: nums = [5] → 5

# nums = [1, 2, 3, -2, 5]
nums = [-3, -1, -2]
# nums = [5]

# def maximum_sum():
#     arr = []
#     for i in range(len(nums)):
#         for n in range(i, len(nums)):
#             arr.append(nums[i]+nums[n])
#     sortedarr = sorted(arr)
#     print(arr)
#     # print(sortedarr[-1])


def maximum_sum():
    max_sum = float("-inf")  # negative infinity — handles the all-negatives trap
    for i in range(len(nums)):  # i = start of the chunk
        current_sum = 0  # reset the running total for each new start
        for j in range(
            i, len(nums)
        ):  # j = end of the chunk, starts AT i (chunk of size 1)
            current_sum += nums[j]  # extend the chunk by one element, add its value
            if current_sum > max_sum:
                max_sum = current_sum
    print(max_sum)
    return max_sum


maximum_sum()
