# what to do i have to return true if on an array their is 2 same number is present and return false if no dublicate number is present

arr = [1, 2, 3, 4]


def findduplicated():
    stack = set()
    for i in arr:
        if i in stack:
            print("True")
            return True
        stack.add(i)
    print("False")
    return False

    # Too Slow
    # length = len(arr)
    # if length <= 0:
    #     print("List is Empty")
    #     return False
    # else:
    #     for num in range(length):
    #         for i in range(num + 1, length):
    #             if arr[num] == arr[i]:
    #                 print("True")
    #                 return True
    #     return False
                

findduplicated()