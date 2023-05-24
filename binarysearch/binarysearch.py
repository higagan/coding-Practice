arr = [1, 2, 4, 5, 6, 74, 99]

def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


print(binary_search(arr, 199))
