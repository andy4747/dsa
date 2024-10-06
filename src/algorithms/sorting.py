def bubble_sort(arr):
    """
    Sort the given array using the bubble sort algorithm.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
