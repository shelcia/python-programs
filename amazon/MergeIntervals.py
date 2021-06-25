# Given a set of time intervals in any order, merge all overlapping intervals into one and
# output the result which should have only mutually exclusive intervals.
# Let the intervals be represented as pairs of integers for simplicity.
# For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8}}.
# The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
# Similarly, {5, 7} and {6, 8} should be merged and become {5, 8}

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Input [[1,4],[2,3]]
# Output [[1,4],[2,3]]
# Expected [[1,4]]


# Time Complexity -> O(nlogn) Space complexity -> O(n)

def mergeInterval(arr):
    arr.sort(key=lambda x: x[0])
    # print(arr)

    mergedInterval = [arr[0]]
    print(mergedInterval)
    k = 0

    for i in range(1, len(arr)):
        # OVERLAPPING INTERVALS
        if(mergedInterval[k][1] >= arr[i][0] and mergedInterval[k][1] <= arr[i][1]):
            mergedInterval.append([mergedInterval[k][0], arr[i][1]])
            mergedInterval.pop(k)
        else:
            # SETS WHICH ARE SUBSETS OF PREVIOUS SET
            if(not (mergedInterval[k][1] >= arr[i][1] and mergedInterval[k][0] <= arr[i][0])):
                k += 1
                mergedInterval.append(arr[i])

    print('merged intervals', mergedInterval)


if __name__ == '__main__':
    arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
    arr2 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    mergeInterval(arr)
    mergeInterval(arr2)
