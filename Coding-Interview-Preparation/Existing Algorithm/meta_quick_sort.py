def quick_sort(arr, low, high):
    if low < high:
        # Partition the array using the chosen pivot
        pi = partition(arr, low, high)

        # Recursively sort the sub-arrays before and after the pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[low]  # Initialize pivot at the leftmost index
    left = low + 1  # Start 'left' pointer one position after the pivot
    right = high  # Start 'right' pointer at the rightmost index (common for leftmost pivot)

    while left <= right:
        # Move 'left' pointer until it finds a value greater than the pivot
        while left <= right and arr[left] <= pivot:
            left += 1

        # Move 'right' pointer until it finds a value smaller than the pivot (or reaches left)
        while left <= right and arr[right] >= pivot:
            right -= 1

        # Swap elements if 'left' and 'right' haven't crossed
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Place the pivot element in its correct position by swapping with the element at 'left-1'
    arr[low], arr[left - 1] = arr[left - 1], arr[low]
    return left - 1  # Return the partition index


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort(arr, 0, len(arr)-1)
print(arr)