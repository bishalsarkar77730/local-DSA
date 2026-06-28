# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

# Given array - [100,4,200,1,3,2]
# find largest consecutive element sequence

# points to solve
# First I have to sort the array, use Insertion Sort



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

data = [100,4,200,1,3,2]
insertion_sort(data)
print("Sorted Array:  ", data)