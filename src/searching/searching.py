def linear_search(arr, target):
    # Your code here


    return -1   # not found


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

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []
binary_search(arr1, -8)
binary_search(arr2, 6)