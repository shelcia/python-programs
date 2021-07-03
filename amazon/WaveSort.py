# Sort an array in wave form

# A Simple Solution is to use sorting. First sort the input array,
# then swap all adjacent elements.
# For example, let the input array be {3, 6, 5, 10, 7, 20}.
# After sorting, we get {3, 5, 6, 7, 10, 20}. After swapping adjacent elements,
# we get {5, 3, 7, 6, 20, 10}.

# Below are implementations of this simple approach.


def WaveSort(arr):
    arr.sort()

    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)


WaveSort([3, 6, 5, 10, 7, 20])  # {5, 3, 7, 6, 20, 10}
WaveSort([3, 6, 5, 10, 7, 20, 11])
