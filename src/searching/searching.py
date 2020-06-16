def linear_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = int((low + high) / 2)
        guess = arr[middle]
        if guess == target:
            return middle
        if guess > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
arr2 = []
linear_search(arr1, -6)