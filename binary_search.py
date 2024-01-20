def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    num_of_iterations = 0
    boundary = None
    while low <= high:
        num_of_iterations += 1
        mid = (low + high) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
            boundary = arr[high + 1]
        else:
            boundary = arr[mid]
            break
    return f"Number of iterations: {num_of_iterations}", f"Boundary: {boundary}"


if __name__ == "__main__":
    some_list = [
        99.2,
        33.4,
        10.3,
        7.5,
        8.6,
        9.99,
        1.2,
        1.03,
        5.4,
        13.89,
        4.2,
    ]
    print(binary_search(sorted(some_list), 13.11))
    print(binary_search(sorted(some_list), 13.89))
    print(binary_search(sorted(some_list), 13.99))
    assert isinstance(binary_search(some_list, 13.11), tuple)
