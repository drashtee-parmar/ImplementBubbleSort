def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # loop  from i = 0 to i = n-1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [5, 8, 3, 9, 4, 1, 7]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
