# Merge Sort

# Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
# It divides the input array into two halves, calls itself for the two halves,
# and then merges the two sorted halves. The merge() function is used for merging two halves.
# The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r]
# are sorted and merges the two sorted sub-arrays into one. See the following C implementation
# for details.

# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:
#              middle m = l+ (r-l)/2
#      2. Call mergeSort for first half:
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)
# The following diagram from wikipedia shows the complete merge sort process
# for an example array {38, 27, 43, 3, 9, 82, 10}. If we take a closer look at the diagram,
# we can see that the array is recursively divided into two halves till the size becomes 1.
# Once the size becomes 1, the merge processes come into action and start merging a

def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr)//2

        i = j = k = 0

        L, R = arr[:mid], arr[mid:]

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            print('cop dat', i, j)
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        mergeSort(L)
        mergeSort(R)
    return arr


# arr = [12, 11, 13, 5, 6, 7, 32, 4, 20, 17, 8]
print(mergeSort([12, 11, 13, 5, 6, 7]))
print(mergeSort([12, 11, 13, 5, 6, 7, 32, 4, 20, 17, 8]))
