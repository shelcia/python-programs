# Find the contiguous subarray within an array, A of length N which has the largest sum.

def findContagious(arr):
    max_sum = arr[0]
    start_ptr = 0
    final_ptr = 1
    current_sum = arr[0]
    start = 0
    print('arr', arr)
    for i in range(1, len(arr)):
        current_sum = current_sum + arr[i]
        if(current_sum > max_sum):
            max_sum = current_sum
            start_ptr = start
            final_ptr = i

        if current_sum < 0:
            current_sum = 0
            start_ptr = i + 1

    print('Maximum Sum:', max_sum)
    print('Contagious Array', arr[start_ptr: final_ptr + 1])


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    findContagious(arr)
