def linear_search(arr, target):
    """
    Perform a linear search on the given array.

    Args:
    arr (list): The list to search through.
    target: The element to search for.

    Returns:
    int: The index of the target if found, -1 otherwise.
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1
