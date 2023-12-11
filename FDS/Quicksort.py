def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]
    return i

def quicksort(arr, left, right):
    if left < right:
        pos = partition(arr, left, right)
        quicksort(arr, pos + 1, right)
        quicksort(arr, left, pos - 1)

arr = [12, 4, 28, 11, 1, 34, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)